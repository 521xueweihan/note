## 起因
今天在写东西的时候，用到了多线程。遇到了个问题：

**子线程的异常，在父线程中无法捕获。**

## 解决

### 问题代码
问题代码示例代码如下：
```python
import threading


class SampleThread(threading.Thread):
    def run(self):
        raise Exception('An error occured here.')


def main():
    try:
        thread_obj = SampleThread()
        thread_obj.start()
    except Exception:
        print 'catch that'

if __name__ == '__main__':
    main()
```

运行输出结果如下：
```
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/path/threading.py", line 810, in __bootstrap_inner
    self.run()
  File "/PycharmProjects/example/threading_example.py", line 15, in run
    raise Exception('An error occured here.')
Exception: An error occured here.
```

### 解决办法
>通过查看资料：http://stackoverflow.com/questions/2829329/catch-a-threads-exception-in-the-caller-thread-in-python

出现上述问题是因为：执行到 `thread_obj.start()` 时，父线程就会立即返回结果。然后，生成的子线程在自己独立的上下文中执行，并使用自己的堆栈。子线程发生的任何异常都是在子线程的上下文中，并且它在它自己的堆栈中（独立于父线程）。

所以，解决办法是：将这些信息传递给父线程。代码如下：
```python
import sys
import threading
import Queue


class ExcThread(threading.Thread):

    def __init__(self, bucket):
        threading.Thread.__init__(self)
        self.bucket = bucket

    def run(self):
        try:
            raise Exception('An error occured here.')
        except Exception:
            self.bucket.put(sys.exc_info())


def main():
    bucket = Queue.Queue()
    thread_obj = ExcThread(bucket)
    thread_obj.start()

    while True:
        try:
            exc = bucket.get(block=False)
        except Queue.Empty:
            pass
        else:
            exc_type, exc_obj, exc_trace = exc
            # deal with the exception
            print exc_type, exc_obj
            print exc_trace

        thread_obj.join(0.1)
        if thread_obj.isAlive():
            continue
        else:
            break


if __name__ == '__main__':
	import sys
import threading
import Queue


class ExcThread(threading.Thread):
    def __init__(self, bucket):
		super(ExcThread, self).__init__()
        self.bucket = bucket

    def run(self):
        try:
            raise Exception('An error occured here.')
        except Exception:
			# 异常信息元祖放入队列传递给父进程
            self.bucket.put(sys.exc_info())


def main():
    bucket = Queue.Queue()
    thread_obj = ExcThread(bucket)
    thread_obj.start()

	# 循环获取子线程的异常信息
    while 1:
        try:
            exc = bucket.get(block=False)
        except Queue.Empty:
            pass
        else:
            exc_type, exc_obj, exc_trace = exc
            # deal with the exception
            print exc_type, exc_obj
            print exc_trace

        thread_obj.join(0.1)
        if thread_obj.isAlive():
            continue
        else:
            break


if __name__ == '__main__':
    main()
```


## 参考
- [catch-a-threads-exception-in-the-caller-thread-in-python](http://stackoverflow.com/questions/2829329/catch-a-threads-exception-in-the-caller-thread-in-python)
