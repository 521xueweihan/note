# 前言
当你看懂了一个技巧的时候，请记得问自己一个问题：这样做的好处是什么呢？

一定要清楚一点，一个特性，技巧的出现。都是为了方便编写更好的程序，或者是解决特定的场景。所以只有知道这样做的好处，才能提升自己的水平。

## 全局变量和局部变量
```python
a = 1  #全局变量

def print_num():
	a = 3  #局部变量
```

## 优化性能
I/O多路复用

[Python网络编程中的select 和 poll I/O复用的简单使用](http://www.cnblogs.com/coser/archive/2012/01/06/2315216.html)

[epoll水平触发，边缘触发](http://www.cnblogs.com/my_life/articles/3968782.html)

[简书：IO多路复用深入浅出](http://www.jianshu.com/p/1020c11f016c)

[How to use linux epoll with python](http://scotdoyle.com/python-epoll-howto.html#blocking-examples)

[更多资料](http://zqdevres.qiniucdn.com/tree/item20100826213130-frameset.html)

## 同步线程
参考：  
1. http://www.cnblogs.com/holbrook/archive/2012/02/23/2365420.html
2. http://www.runoob.com/python/python-multithreading.html
3. 简述上面的简单的例子：http://www.jianshu.com/p/86b8e78c418a
4. 廖雪峰教程中的多线程：http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832360548a6491f20c62d427287739fcfa5d5be1f000
5. IBM线程池，等优化：https://www.ibm.com/developerworks/cn/aix/library/au-threadingpython/

## GIL
参考：http://cenalulu.github.io/python/gil-in-python/

## 线程安全
参考：https://www.zhihu.com/question/23030421

## 魔法方法
python中的魔法方法：就是一个行为，默认调用的方法，而这个方法python语言已经默认写好了。如果你不重写这个方法，那么就会调用默认写好的方法。

比如，`print`默认调用的就是`__str__`方法，f是一个函数，`f()`默认调用就是`__call__()`方法，这些都叫做‘魔法方法’：
```python
class A(object):
	def __str__(self):
		return 'A'
	def __call__(self):
		return 'A call()'
a = A()
print a  # A
a()   # A call()

```

## 惰性求值
返回值是一个函数，当需要的到结果，调用`__call__()`方法，就会得到真正的结果。这样的行为叫做`惰性求值`：
```python
def lazy_sum(nums):
	def _sam():
		return reduce(lambda x, y: x+y, nums)
	return _sam

t = lazy_sum([1,2,3])
t   # <function __main__._sum> 这个时候t是一个函数
t()  # 6，惰性求值就是利用闭包返回一个函数
```

输入`t.__call__()`试试，其实`t()`调用的就是魔法方法`__call__()`

## 闭包
在python中函数是对象，可以作为参数。所以就是出现了：
```python
def func1():
	print 'This is func1.'

def func2(func):
	func()
	print '上面调用了func1，我是func2！'

func2(func1)  
# This func1.
# 上面调用了func1，我是func2！

```
而闭包就是：函数func1调用函数func2中的参数。
```python
def func1(name):
	print "This is %s" % name

def func2(func):
	name = func.__name__+'!'
	func(name)  # 传入的func调用了func2中的变量name

func2(func1)
# This is func1!
```
闭包可以用来实现惰性求值；  
闭包就是**携带状态的函数**，并且它的状态可以完全对外隐藏起来。

## staticmethod、classmethod、实例方法
```python
class A(object):
	def a(self):
		print '实例方法'

	@classmethod
	def b(cls):
		print 'classmethod'

	@staticmethod
	def c():
		print 'staticmethod'

t1 = A()  # t1为实例，下面分别调用：实例方法、类方法、静态方法
t1.a() # 实例方法
t1.b() # classmethod
t1.c() # staticmethod

t2 = A # t2为类，下面分别调用：实例方法、类方法、静态方法
t1.a() # 报错：unbound method a() must be called with A instance as first argument (got nothing instead)
t1.b() # classmethod
t1.c() # staticmethod
```
结论：通过上面的代码可知，实例可以调用：实例方法、类方法、静态方法。类只可以调用：类方法、静态方法。
同理，实例可以调用类属性，但是类不可以调用实例属性。

## 方法和函数
**第一种解释：在一个对象中绑定函数，称为这个对象的方法。**

函数(function):  
它是一段代码，通过名字来调用。它可以将一些参数传递进去然后处理，最后返回数据，或者不返回数据也行

方法(method):  
它也是一段代码，通过名字来调用。同时可以传入参数然后处理，**不同的是参数是对象的属性**。

也就是说：在python中，方法就是实例方法和类方法和静态方法。函数就是普通的方法（不再类里面的方法）

在python代码中的体现为：

```python
class Programer(object):
    def __init__(self, name):
        self.name = name

    def show_name(self):
        '''这个是method，因为它传入的参数是对象的属性'''
        print self.name

def show_something2(something):
    '就是这个意思'
    print something
```

## 什么是哈希表和哈希算法
哈希算法并不是一个特定的算法而是一类算法的统称。哈希算法也叫散列算法，一般来说满足这样的关系：f(data)=key，输入任意长度的data数据，经过哈希算法处理后输出一个定长的数据key。同时这个过程是不可逆的，**无法由key逆推出data**。

如果是一个data数据集，经过哈希算法处理后得到key的数据集，然后将keys与原始数据进行一一映射就得到了一个哈希表。一般来说哈希表M符合M[key]=data这种形式。(这就是为什么字典的key需要为不可变的数据，因为需要用key来计算value的地址，如果key相同则会造成混乱。集合中不会有相同的数据。)

哈希表的好处是当原始数据较大时，我们可以用哈希算法处理得到定长的哈希值key，那么这个key相对原始数据要小得多。我们就可以用这个较小的数据集来做索引，达到快速查找的目的。

稍微想一下就可以发现，既然输入数据不定长，而输出的哈希值却是固定长度的，这意味着哈希值是一个有限集合，而输入数据则可以是无穷多个。那么建立一对一关系明显是不现实的。所以"碰撞"(不同的输入数据对应了相同的哈希值)是必然会发生的，所以一个成熟的哈希算法会有较好的抗冲突性。同时在实现哈希表的结构时也要考虑到哈希冲突的问题。

密码上常用的MD5，SHA都是哈希算法，因为key的长度(相对大家的密码来说)较大所以碰撞空间较大，有比较好的抗碰撞性，所以常常用作密码校验。
