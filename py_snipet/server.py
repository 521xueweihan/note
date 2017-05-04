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

while 1:
    data = conn.recv(1024)  # 接受TCP数据，1024表示缓冲区的大小
    if not data: break
    print '接收到：', repr(data)
    conn.sendall('Done')  # 把从客户端接收来的数据完整的，发送给客户端
conn.close()   
