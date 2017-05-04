# 再学 socket 之非阻塞 Server
> 本文是基于 python2.7 实现，运行于 Mac 系统下

本篇文章是上一篇[初探 socket](http://www.cnblogs.com/xueweihan/p/5445483.html) 的续集，
上一篇文章介绍了：如何建立起一个基本的 socket 连接、TCP 和 UDP 的概念、socket 常用参数和方法

Socket 是用来通信、传输数据的对象，上一篇已经研究了如果进行基本的通行和传输数据。因为，在这个互
联网爆发的时代，做为 Server 的 socket 要同时接收很多的请求。

**通过阅读：[地址](https://ruslanspivak.com/lsbaws-part3/)，强烈推荐阅读原文。**

整理了下面的文字，如何：创建一个 非阻塞的 server。


## 一、阻塞 Server
- 阻塞 Server 示例
- 为什么会出现阻塞

### 1.1 阻塞 Server 示例
下面就通过`C/S`模型，展示阻塞状态：
- 接收其它 socket 请求的 socket 叫做：Server（S）
- 请求 Server 的 socket 叫做：Client（C）

该代码片段分别是：阻塞的 Server 和测试用的 Client：
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   
#   Author  :   XueWeiHan
#   Date    :   17/2/25 上午10:39
#   Desc    :   阻塞 server
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '', 50007
REQUEST_QUEUE_SIZE = 5


def handle_request(client_connection):
    """
    处理请求
    """
    request = client_connection.recv(1024)
    print('Server recv: {request_data}'.format(request_data=request.decode()))
    time.sleep(10)  # 模拟阻塞事件
    http_response = "Hello, I'm server"
    client_connection.sendall(http_response)


def server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Server on port {port} ...'.format(port=PORT))

    while 1:
        client_connection, client_address = listen_socket.accept()
        handle_request(client_connection)
        client_connection.close()

if __name__ == '__main__':
    server()

```
- `REQUEST_QUEUE_SIZE`：在 sever 阻塞的时，允许挂起几个连接。便于可以处理时直接从该队列中取得连接，减少建立连接的时间
- `time.sleep`：用于模拟阻塞

测试用的 Client
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   
#   Author  :   XueWeiHan
#   Date    :   17/2/25 上午11:13
#   Desc    :   测试 client

import socket

SERVER_ADDRESS = (HOST, PORT) = '', 50007


def send_message(s, message):
    """
    发送请求
    """
    s.sendall(message)


def client():
    message = "Hello, I'm client"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    send_message(s, message)
    print 'Client is Waiting response...'
    data = s.recv(1024)
    s.close()
    print 'Client recv:', repr(data)  # 打印从服务器接收回来的数据

if __name__ == '__main__':
    client()

```
打开三个终端，先运行 Server，在另外两个终端运行 Client（分别起名为client1、client2），会发现
服务器先接收 client1 的数据，然后返回响应。再此之前 client2 一直处于等待的状态。只有等 Server
处理完 client1 的请求后，才会接收 client2 的数据。

![](http://images2015.cnblogs.com/blog/759200/201704/759200-20170414163035517-1756451179.gif)


**这样一个个地接收请求、处理请求的 Server 就叫做 阻塞 Server。**


### 1.2 为什么会出现阻塞？
因为服务器处理请求是需要消耗时间的，正如我上面的阻塞 Server 代码中的`time.sleep(10)`，用于模拟
服务器处理请求消耗的时间。

在处理完上一个请求（返回给 Client 数据）的这段时间中，服务器无法处理其它的请求，只能让其它的 Client 等待。这样的效率是
极其低下的，所以下面就介绍如何创建一个非阻塞的 Server

## 二、非阻塞 Server
- 需要知道的一些基本概念
- 非阻塞 Server 示例（多进程）

后面会用**多进程**实现 非阻塞socket，在此之前需要了解一些基本知识和概念，便于理解后面的代码。

### 2.1 需要知道的一些基本概念
- Socket 处理请求的过程
- 进程
- 文件描述符
- 如何查看进程和用户资源

#### 2.1.1 Socket 处理请求的过程
参照上面写的阻塞 Server 的代码，可以看出：服务器端的socket对象，`listen_socket` 从不和客户端交换数据。它只会通过`accept`方法接受连接。然后，创建一个新的socket对象，`client_connection`用于和客户端通信。

所以，服务器端的socket 分为：**接受请求的socket（listen_socket）** 和 **与客户端传输数据的socket（client_connection）**。

正如上面说到的，真正阻塞地方是：与客户端传输数据的socket（`client_connection`） 需要等待处理请求的结果，然后返还给客户端，结束这次通信，才能处理后面的请求。

#### 2.1.2 进程
存在硬盘中的叫做‘程序’（\*.py），当程序运行加载到内存中的时候叫做‘进程’。系统会分配给每个进程一个唯一 ID，
这个 ID 叫做：PID ，进程还分为父进程和子进程，父进程（PPID）创建子进程（PID）。关系如下图：

![](http://images2015.cnblogs.com/blog/759200/201704/759200-20170414163215064-1420067890.png)


可以通过`ps`命令来查看进程的信息：[每天一个linux命令（41）：ps命令](http://www.cnblogs.com/peida/archive/2012/12/19/2824418.html)

**需要注意：**
- 子进程一定要关闭
- 子进程关闭一定要通知父进程，否则会出现‘僵尸进程’
- 一定要先结束父进程，再结束子进程，否则会出现‘孤儿进程’

**僵尸进程**：一个进程使用fork创建子进程，如果子进程退出，而父进程并没有调用wait或waitpid获取子进程的状态信息，那么子进程的进程描述符仍然保存在系统中。这种进程称之为僵尸进程。（系统所能使用的进程号是有限制的，如果大量的产生僵死进程，将因为没有可用的进程号而导致系统不能产生新的进程。则会抛出`OSError: [Errno 35] Resource temporarily unavailable`异常）

**孤儿进程**：一个父进程退出，而它的一个或多个子进程还在运行，那么那些子进程将成为孤儿进程。孤儿进程将被init进程(进程号为1)所收养，并由init进程对它们完成状态收集工作。（没有危害）


#### 2.1.3 文件描述符
在UNIX中一切都是一个文件，当操作系统打开一存在的个文件的时候，便会返回一个‘文件描述符’，进程通过
操作该文件操作符，从而实现对文件的读写。Socket 是一个操作文件描述符的进程，Python 的 socket
模块提供了这些操作系统底层的实现。我们只需要调用`socket`对象的方式就可以了。

**需要注意**：
- 文件描述符的回收机制是采用**引用计数方式**
- 每次操作完文件描述符需要调用`close()`方法，关闭文件描述符。道理和进程一样，操作系统都会最多可创建的文本描述符的限制，如果一直不关闭文本描述符的话，导致数量太多无法创建新的，就会抛出`OSError: [Errno 24] Too many open file`异常。


#### 2.1.4 如何查看进程和用户资源极限
计算机的计算和存储能力都是有限的，统称为计算机资源。

上面说了进程和文件描述符号都是有个**最大数量**（极限），下面就是用于查看和修改用户资源限制的命令——`ulimit`。

```
-a	列出所有当前资源极限。
-c	以 512 字节块为单位，指定核心转储的大小。
-d	以 K 字节为单位指定数据区域的大小。
-f	使用 Limit 参数时设定文件大小极限（以块为单位），或者在未指定参数时报告文件大小极限。缺省值为 -f 标志。
-H	指定设置某个给定资源的硬极限。如果用户拥有 root 用户权限，可以增大硬极限。任何用户均可减少硬极限。
-m	以 K 字节为单位指定物理内存的大小（驻留集合大小）。系统未强制实施此限制。
-n	指定一个进程可以拥有的文件描述符数的极限。
-r	指定对进程拥有线程数的限制。
-s	以 K 字节为单位指定堆栈的大小。
-S	指定为给定的资源设置软极限。软极限可增大到硬极限的值。如果 -H 和 -S 标志均未指定，极限适用于以上二者。
-t	指定每个进程所使用的秒数。
-u	指定对用户可以创建的进程数的限制。
```

常用命令如下：
- `ulimit -a`：查看
- `ulimit -n`：设置一个进程可拥有文件描述符数量
- `ulimit -u`：最多可以创建多少个进程

### 2.2 Fork 方式的非阻塞 Server
采用 fork 的方式实现非阻塞 Server，主要原理就是当 socket 接受到（accept）一个请求，就 fork 出一个子进程
去处理这个请求。然后父进程继续接受请求。从而实现并发的处理请求，不需要处理上一个请求才能接受、处理下一个请求。

```python
import errno
import os
import signal
import socket

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 1024


def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                 os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            # restart 'accept' if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()  # close parent copy and loop over

if __name__ == '__main__':
    serve_forever()
```
如阅读代码时出现的问题，可以参考下面的关键字：

1. Python os.fork，文件句柄（引用计数）、子进程（pid==0）
2. [linux ulimt命令](http://bian5399.blog.51cto.com/3848702/963662)
3. [僵尸进程](http://www.cnblogs.com/Anker/p/3271773.html)，[如何避免僵尸进程](http://www.cnblogs.com/yuxc/archive/2012/11/04/2753391.html)，采用`os.wait`。
4. [python signal模块](http://brieflyx.me/2015/python-module/python-signal-module/#)
5. [error.EINTR](http://blog.csdn.net/tigerjibo/article/details/11695673)（慢系统调用：可能永远阻塞的系统调用，例如：socket）
6. 因为过多的子进程并发开始，同时结束，会并发的发出结束的信号，父进程的 signal 一瞬间接收过多的信号，导致了有的信号丢失，这种情况还是会遗留一些僵尸进程。这个时候就需要写一个handle信号的方法。采用`waitpid`的`os.WHOHANG`选项，进行死循环。以确保获取到所有 signal
7. OSError 因为`waitpid`的`os.WNOHANG`选项，不会阻塞，但是如果没有子进程退出，会抛出`OSError`，需要 catch 到这个异常，保证父进程接收到了每个子进程的结束信息，从而保证没有僵尸进程。

```
waitpid()函数的options选项：

os.WNOHANG - 如果没有子进程退出，则不阻塞waitpid()调用

os.WCONTINUED - 如果子进程从stop状态变为继续执行，则返回进程自前一次报告以来的信息。

os.WUNTRACED - 如果子进程被停止过而且其状态信息还没有报告过，则报告子进程的信息。
```

## 最后
该非阻塞 Server 是通过操作系统级别的 fork 实现的，用到了多进程和信号机制。

因为多进程解决非阻塞的问题，很好理解，但是十分消耗计算机资源的，后面会介绍更加轻量级的——利用事件循环实现非阻塞 Server。

挖个坑～

## 参考
- [什么是孤儿进程、僵尸进程](http://www.cnblogs.com/Anker/p/3271773.html)
- [linux 如何清理僵尸进程](http://www.cnblogs.com/yuxc/archive/2012/11/04/2753391.html)
- [什么是pid、ppid](https://delightlylinux.wordpress.com/2012/06/25/what-is-pid-and-ppid/)
- [ulimit 命令](https://www.ibm.com/support/knowledgecenter/zh/ssw_aix_72/com.ibm.aix.cmds5/ulimit.htm)
