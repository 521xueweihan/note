## 目录


# 三、在UDP上建立虚拟连接

## 介绍
UDP是无连接的，一个UDPsocket可以被用做，与任意数量的计算机交换数据包。然而，在多人游戏中，我们只希望在一小部分建立起连接的计算中，交换数据包。

所以，我们需要做的第一步就是：在UDP上让两台计算机，建立起虚拟连接。

但是，首先，我们先深入到底层，弄清楚互联网是如何工作的。

## 互联网不是一系列的电话线
在2006年， Senator Ted Stevens做了一个互联网历史上，著名的一次演讲：
>“The internet is not something that you just dump something on. It’s not a big truck. It’s a series of tubes”

当我第一次使用互联网的是：1995年，我在大学的计算机实验室中，我用Netscape浏览器上网，当时漫无目的的瞎逛。

我当时想：每次连上一个网站，就产生一些“真实的连接”，就像电话线。我十分惊奇，当我每次访问一个新的网站的时候需要花费多少钱？（作者当时认为，每次访问网站都是建立在一条通信线路之上，就像电话线，需要拉线）不会有人找上门，让我付这些线路的费用吧？

当然，这个想法现在看起来很傻。

## 没有直接的连接
互联中：没有一条通信电缆，直接通信的两台计算机。数据是由IP协议，通过数据包，从一个个电脑传递过来的。（就像传纸条）

一个数据包可能通过几个计算机才能到达目的地。你不能知道准确的传递过程（第一步，第二步。。。），这个过程是会变化的，是根据网络质量决定数据包的下一步走向。你可能发送过两个数据包A和B到同一个地址，它们可能走的是不同的路线。这个也是数据包无序的一个原因。

在Linux和Unix系统上（win可以用‘tracert’），可以使用‘traceroute’指令来查看数据包的传递线路和途径的主机名和IP地址。[traceroute请参考](http://www.cnblogs.com/peida/archive/2013/03/07/2947326.html)

试一下`traceroute`指令：
```
traceroute: Warning: baidu.com has multiple addresses; using 220.181.57.217
traceroute to baidu.com (220.181.57.217), 64 hops max, 52 byte packets
 1  192.168.1.1 (192.168.1.1)  4.727 ms  4.960 ms  4.144 ms
 2  223.20.160.1 (223.20.160.1)  13.405 ms  6.047 ms  8.561 ms
 3  218.241.252.185 (218.241.252.185)  4.735 ms  2.130 ms  7.771 ms
 4  218.241.252.197 (218.241.252.197)  6.849 ms  5.335 ms  4.555 ms
 5  202.99.1.217 (202.99.1.217)  4.025 ms  13.324 ms  3.761 ms
 6  * 218.241.244.21 (218.241.244.21)  8.492 ms
    218.241.244.9 (218.241.244.9)  5.389 ms
 7  218.241.244.33 (218.241.244.33)  6.699 ms  4.851 ms  5.386 ms
 8  * * *
```
注意：第八行是因为有[ICMP](http://baike.baidu.com/item/ICMP)防火墙，请求被拒绝了，所以没有探测出目的ip地址。

这个过程就能诠释：没有直接的连接。

## 如何收到数据包
正如[前一篇文章]()，举的那个简单的例子：收到数据包，就像在一个房间，人们手递手传纸条。

互联网是网络的网络（网络的集合）。当然我们不仅在一个小房子中传递信件，我们能把它传到世界各地。

最好的例子是邮局系统！

当你想要发一封信给别人，你需要把你的信放到邮箱中，同时你会相信会到达收件人的手上。信件怎么到的，你不需要关心，反正到了。总得有人把你的信送到目的地，那么到底是怎么送到的呢？

首先，邮递员不会拿着你的信，直接送到目的地！邮递员拿着你的信，送到当地邮局，让邮局处理。

如果这封信是本地的，本地的邮局会收过来，安排让另外一个邮递员直接送到目的地。但是，如果信的地址不是本地的，那么本地的邮局不会直接把信送到目的地，所以邮局会送到上一级（镇邮局送到市邮局），或者送到临近城市的邮局，如果目的地太远就会送到飞机场。信件的传输方式是用大卡车。

我们来看一个例子：假定一封信，从洛杉矶寄到北京，本地邮局接收到信，然后发现是国际信件，就直接送到洛杉矶的邮件中心。这封信，确认收件的地址无误，就安排到下一班飞机飞往北京的航班。

飞机着陆在北京，北京的邮件系统肯定是和洛杉矶的邮件系统不一样。北京的邮件中心收到这封信后，就送到具体的区级的当地邮局，最终，这封信会通过一个邮递员直接送到收件人的手里。

就像邮局系统，通过地址传递信件一样。网络传递数据包是通过IP地址。传递数据包的细节和路径选择是非常复杂的，但是基本思想：每个路由器都是一台计算机，由路由表决定数据下一步走的地址。(这部分我省略了一些路由和路由表的部分，我没有看懂，后面研究明白，回来再补全。现在不影响后面的阅读)

编辑路由表的工作是网络管理员的工作，不是我们这些程序员关心的问题（还好😋）。但是，如果你想了解更多关于这方面的知识，可以看看下面这些文章：
- [ars technica](http://arstechnica.com/features/2008/09/peering-and-transit/)：讲网络如何交换数据包和传输的细节
- [routing tables](http://www.faqs.org/docs/linux_network/x-087-2-issues.routing.html)
- [border gateway protocol](https://en.wikipedia.org/wiki/Border_Gateway_Protocol)

## 虚拟连接
现在回到连接的话题上。

如果你使用TCP socket，你知道它是面向连接的，看起来像一个‘连接’。但是TCP是建立在IP协议上的，而IP协议只是数据包在计算机之间传递（并没有连接的概念），所以TCP的连接概念一定是：虚拟连接。

如果TCP可以建立再IP上建立虚拟的连接，那么我们也能在UDP上实现虚拟连接。

让我们定义虚拟连接：两台计算机间传输UDP数据包以固定的速度，如每秒10个包。只要数据包传输流畅，我们就认为：两个计算机建立起了虚拟连接。

连接分为两部分：
- 监听计算机连入，我们称这个计算机为‘服务器’。
- 通过IP地址和端口连接服务器的计算机，我们成为‘客户端’。

我们把场景设定为（先设定简单的场景，一点点来）：不论何时，我们只允许一个客户端连接服务器。同时，我们假定服务器的IP地址不变，客户端是直接连接服务器。后面的文章再说支持多个客户端连接的例子等，现在先现实我们限定条件下，简单的虚拟连接，这样可以更好的理解虚拟连接。

## 协议id
UDP是无连接的，UDP socket会接收任意计算机发来的数据包。

我们将限定：服务器只从客户端接收数据包，客户端只给服务器发送数据包（一对一）。我们不能通过地址过滤数据包，因为服务器不知道客户端的地址（python中socket可以通过recvfrom方法得到地址）。所以我们在每个UDP数据包加一个‘头信息’，由32位protocol id组成：
```
[uint protocol id]
(packet data...)
```
protocol id只是一些唯一的数字。如果数据包的protocol id不能匹配我们的protocol id，数据包就被忽略。如果protocol id匹配，我们就接收packet data。

你只需要选择唯一的数字，可以用hash你的游戏名字和协议版本数字。你也可以用任何信息当做protocol id，需要保证protocol id的唯一性，因为这个protocol id是我们连接协议的基础。


## 检测连接
现在我们需要一个检查连接的方法。

当然我们可以做一些复杂的握手，此过程需要发送和接收多个UDP数据包。或许客户端‘请求连接’数据包，发送服务器，服务器响应返回给客户端‘连接接受’，或者如果客户端请求与，已经和其他客户端建立起连接的服务器，建立连接，则服务器就会返回给客户端‘忙碌中’。

或者，我们可以让服务器检查接收到的第一个数据包的protocol id是否正确，然后考虑是否建立连接。

客户端假定与服务器建立起连接，然后给服务器发送数据包。当服务器接受到客户端发来的第一个数据包，就记下该客户端的IP地址和端口号，最后，返回响应数据包。

客户端已经知道服务器的地址和端口。所以，当客户端接受数据包，客户端会过滤掉任何不是服务器地址的请求。同样，服务器接收到客户端的第一个数据包，通过`recvfrom`方法，能获取到客户端的IP地址和端口。所以服务器也可以忽略不来自指定客户端的任何数据包。

我们可以使用这个简洁的方式，因为我们只需要在两台计算机之间建立连接。在后面的文章中，我们会升级我们的连接系统，用于支持两个以上的计算机连接，并且使得连接更加健壮。

（就是与特定ip地址和端口的计算机进行传输数据）

## 检测断开连接
我们如何检测断开连接？

如果一个连接被定为接收数据包，那么断开连接就可以定义为不接收数据包。

为了查明我们没有接受数据包，服务器和客户端两边都计算：从上一次接收到数据包的开始，到下一个接收到数据包的时间。（也就是所谓的‘超时时间’）

每次如果我们接收到数据包，就重置计时器（’超时时间’清零）。如果计时器超过设定的值，侧连接‘超时’，我们就是断开连接（不再限制连接客户端的IP和端口）。

这也是一种优雅的方式用来处理，第二个客户端请求已建立连接的服务器的情况。建立起连接的服务器不会接收来自其他客户端的数据包，所以第二个客户端接收不到服务器响应的数据包，所以第二个客户端连接超时并处于断开连接的状态。

## 总结
这些就是建立虚拟连接的过程：建立连接，过滤不是来自连接的计算机的数据包，检查断开连接，设定超时。

我们的建立的连接跟其他TCP连接一样，稳定的UDP数据包传输是多人动作游戏的基础。

目前为止，已经在UDP上建立虚拟的连接，你就可以使用它来进行多人游戏中的，client/server模式下的数据传输，来替代TCP。

每次只允许有一个连接。有一个超时的时间，用于释放连接。释放后，可以建立新的连接。

## python实现
看完理论部分，下面我就用python根据上述原理实现：我写的UDP上实现虚拟连接只做了两件事：每次只能有一个socket和server进行通信；如果在一段时间无数据传输，则注销掉原来的连接，允许建立新的连接。
- protocol id：我打算用时间戳hash一个字符串
- 监测超时通过`settimeout()`方法，捕获socket.timeout异常

test_server.py
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/5/11 下午3:54
#   Desc    :   server

import socket
import time

UDP_IP = ''
UDP_PORT = 5000
_ID = []  # 存储建立连接的protocol_id
_IP = None  # 存储建立连接的IP和端口
TIME_OUT = 2  # 超时时间(s)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(TIME_OUT)

def check_protocol_id(protocol_id, _ID):
	'''
	检测protocol_id
	'''
	if _ID:
		if protocol_id in _ID:
			return True
		else:
			return False
	else:
		_ID.append(protocol_id)
		return True

print '准备接收内容。'
while 1:
	try:
		response = ''
		data, addr = sock.recvfrom(1024)  # 缓冲区大小为1024bytes
		protocol_id, data = data.split('|')
		if _IP:
			if _IP == addr:
				response = '建立连接'
				print '从{ip}:{port}，接收到内容：{data}'.format(ip=addr[0],
															   port=addr[1], data=data)
			else:
				response = '无法建立连接'
		else:
			if check_protocol_id(protocol_id, _ID):
				_IP = addr
				response = '建立连接'
				print '从{ip}:{port}，接收到内容：{data}'.format(ip=addr[0],
															   port=addr[1], data=data)
			else:
				response = '无法建立连接'
		# 返回响应数据包给客户端
		sock.sendto(response, addr)
	except socket.timeout:
		print '连接超时，注销连接，其他socket可以连入'
		_IP = None
		_ID = []
```

test_client.py
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/5/11 下午3:54
#   Desc    :   client
import socket
import time
import hashlib

UDP_IP = ''
UDP_PORT = 5000
MESSAGE = 'Hello, world!'
TIME_OUT = 3

print 'UDP 目标IP：', UDP_IP
print 'UDP 目标端口：', UDP_PORT
print '发送的内容：', MESSAGE

class Udp(object):
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server_addr = None
        # 设置超时时间
		self.socket.settimeout(TIME_OUT)

	@property
	def protocol_id(self):
		hash = hashlib.md5(str(time.time()) + 'xueweihan')
		return hash.hexdigest()

	def send_mesaage(self):
		# 这里只简单用｜分割protocol_id和发送内容
		message = self.protocol_id +'|'+ MESSAGE
		self.socket.sendto(message, (UDP_IP, UDP_PORT))

	def get_message(self):
		data, addr = self.socket.recvfrom(1024)
		if self.server_addr:
			# 客户端也只接收建立连接的服务端的数据包
			if self.server_addr == addr:
				return data
			else:
				return None
		else:
			self.server_addr = addr
			return data

s1 = Udp()
for i in range(2):
	try:
		s1.send_mesaage()
		print s1.get_message()
	except socket.timeout:
		print '连接超时'
		# 清除原来建立连接的数据
        s1.server_addr = None        

s2 = Udp()
for i in range(2):
# 此时是无法建立连接的，因为上一个连接还没有销毁
	try:
		s2.send_mesaage()
		print s2.get_message()
	except socket.timeout:
		print '连接超时'
		# 清除原来建立连接的数据
        s2.server_addr = None

# 暂停2秒，等待服务器注销上一次的连接
time.sleep(2)
s3 = Udp()
for i in range(2):
# 此时是可以建立连接的，因为上面连接以超时
	try:
		s3.send_mesaage()
		print s3.get_message()
	except socket.timeout:
		print '连接超时'
		# 清除原来建立连接的数据
        s3.server_addr = None

```
上面代码还有很多不足的地方，所以仅供参考。所有代码都在[github](https://github.com/521xueweihan/udp_socket)上，代码运行效果如下：
![](http://7xqirw.com1.z0.glb.clouddn.com/udp%20virtual%20connect.gif)
