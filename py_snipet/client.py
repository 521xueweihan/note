# coding: utf-8
import socket

print '我是客户端！'
HOST = 'localhost'    # 服务器的ip
PORT = 50007              # 需要连接的服务器的端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print "发送'Hello world',到服务器"
s.sendall('Hello, world')  # 发送‘Hello，world’给服务器
data = s.recv(1024)
s.close()
print '接收到', repr(data)  # 打印从服务器接收回来的数据
