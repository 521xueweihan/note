## 1.什么是socket？
Socket中文译作：套接字，但是大家一般约定俗称的都用：socket。我想在解释socket是什么之前，先说它是用来干嘛的：socket是来建立‘通信’的基础，建立连接，传输数据————‘通信端点’。

我的理解：每个socket对象就是一个抽象的‘通信对象’，而‘通信对象’做的事情就是发送或者接受信息。就想生活中：每个联网的计算机就是一个socket对象，每个打电话的人也是一个socket对象。

每个编程语言几乎都现成的socket类，为什么？你见过不能上网的计算机吗～有了socket类，我们只需要调用这个类就能愉快的进行网络编程了，也就是接下来要说的：python中的socket编程。

## 2.python中的socket编程
正如上面说的一样，socket是传输数据的，传输数据是如何传送？要效率还是要准确性？所以socket分为两种：面向连接和无连接。

1. 面向连接：使用的TCP协议，就是在传输数据之前，先建立可靠的连接，然后数据以字节流的形式传输。从而保证了数据的可靠、不重复、有序性。因为是字节流，所以没有数据边界，可以把一份数据拆分成多份，这样有利于传输的效率。

2. 无连接：使用的UDP协议，传输数据之前不需要建立连接，数据以报文的形式传输。

**总结**： 两者的区别在于——是否建立连接；数据传输的形式（报文或者数据流）

### TCP Socket
TCP Socket通信流程图：
![](http://7xqirw.com1.z0.glb.clouddn.com/socket_follow.png)

下面就是使用python语言，编写服务器端的例子：

```python
# coding: utf-8
#  服务器端代码
import socket

print '我是服务端！'
HOST = ''                 
PORT = 50007              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP socket对象
s.bind((HOST, PORT))  # 绑定地址
s.listen(1)  # 监听TCP，1代表：最多允许1个连接同时连进来
conn, addr = s.accept()  # 开始被动接受TCP客户端的连接。
print '连接的地址', repr(addr)
while 1:
    data = conn.recv(1024)  # 接受TCP数据，1024表示缓冲区的大小
    if not data: break
	print '接收到:', repr(data)
    conn.sendall(data)  # 把从客户端接收来的数据完整的，发送给客户端
conn.close()  
```
现在服务器端的TCP socket已经开始监听：50007端口，等待客户端的连接。接下来就是写客户端的socket，让这两个soket连接起来，产生通信。

```python
# coding: utf-8
import socket

print '我是客户端！'
HOST = 'localhost'    # 服务器的ip
PORT = 50007              # 需要连接的服务器的端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print "发送'hello world'"
s.sendall('Hello, world')  # 发送‘Hello，world’给服务器
data = s.recv(1024)
s.close()
print '接收到', repr(data)  # 打印从服务器接收回来的数据
```
让他们跑起来：
1. `python server.py`，先运行服务器端的代码
2. 再开一个终端，`python client.py`，运行客户端的代码
3. 结果如下：
![](http://7xqirw.com1.z0.glb.clouddn.com/socket.gif)

### UDP Socket
UDP是无连接，同时发送的是报文，所以和TCP Socket有一些不一样的地方，参照下面socket的方法和属性表，修改上面的代码就可以了。

#### 1.Socket类型
套接字格式：  
socket(family, type[,protocal])使用给定的地址族、套接字类型、协议编号（默认为0）来创建套接字。

**地址族**

| 地址族    | 描述     |
| :------------- | :------------- |
| socket.AF_UNIX       | 只能够用于单一的Unix系统进程间通信(本地通信)       |
| socket.AF_INET      | 服务器之间网络通信       |
| socket.AF_INET6      | 使用IPv6地址，进行通信   |

**套接字类型**

| 套接字类型 | 描述  |
| :------------- | :------------- |
| socket.SOCK_STREAM      | 流式socket，用于TCP       |
| socket.SOCK_DGRAM      | 数据报式socket，用于UDP      |

**实例**

| 实例     | 描述     |
| :------------- | :------------- |
| 创建TCP Socket       | s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      |
| 创建UDP Socket       | s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      |

#### 2.Socket函数
1. TCP发送数据时，已建立好TCP连接，所以不需要指定地址。UDP是面向无连接的，每次发送要指定是发给谁。
2. 服务端与客户端不能直接发送列表，元组，字典。只能传字符串(repr(data)或str(data))。

**服务端socket函数**

| 服务端socket函数     | 描述    |
| :------------- | :------------- |
| s.bind(address)      | 将套接字绑定到地址, 在AF_INET下,以元组（host,port）的形式表示地址.       |
| s.listen(backlog)    | 开始监听TCP传入连接。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。 |
| s.accept()    | 接受TCP连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。|

**客户端socket函数**

| 客户端socket函数     | 描述     |
| :------------- | :------------- |
| s.connect(address)       | 连接到address处的套接字。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
| s.connect_ex(adddress)       | 功能与connect(address)相同，但是成功返回0，失败返回errno的值。      |

**公共socket函数**

| 公共socket函数     | 描述     |
| :------------- | :------------- |
| s.recv(bufsize[,flag])       | 接受TCP套接字的数据。数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。     |
| s.send(string[,flag]) | 发送TCP数据。将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。 |
| s.sendall(string[,flag]) | 完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。 |
| s.recvfrom(bufsize[.flag]) | 接受UDP套接字的数据。与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。 |
| s.sendto(string[,flag],address) | 发送UDP数据。将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。 |
| s.close() | 关闭套接字。 |
| s.getpeername() | 返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。 |
| s.getsockname() | 返回套接字自己的地址。通常是一个元组(ipaddr,port) |
| s.setsockopt(level,optname,value) | 设置给定套接字选项的值。 |
| s.getsockopt(level,optname[.buflen]) | 返回套接字选项的值。 |
| s.settimeout(timeout) | 设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()） |
| s.gettimeout() | 返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。 |
| s.fileno() | 返回套接字的文件描述符。 |
| s.setblocking(flag) | 如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。 |
| s.makefile() | 创建一个与该套接字相关连的文件 |

### TODO
粘包，分包，非阻塞socket，实现全双工？

### 参考
- [杨云1028 的BLOG](http://yangrong.blog.51cto.com/6945369/1339593)
- [Python Socket HowTO](https://docs.python.org/2.7/howto/sockets.html)
- [Python Socket官方文档](https://docs.python.org/2/library/socket.html)
