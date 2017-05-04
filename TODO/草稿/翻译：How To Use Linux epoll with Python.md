> [How To Use Linux epoll with Python](http://scotdoyle.com/python-epoll-howto.html)

## 目录
－ 前言
－ 阻塞 Socket 例子
－ 异步 Socket 和 epoll 的益处
－ 使用 epoll 的异步 Socket 例子
－ 性能注意事项
－ 源码

## 一、前言
Python 从 2.6 版本引入了 Linux 的 epoll 库，不知道这个库是个什么鬼没关系，下面我会一一道来，本文
中的所有示例代码，均在 Python2.7.10 下执行演示。

## 二、阻塞 Socket 例子
```python
import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)

connectiontoclient, address = serversocket.accept()
request = b''
while EOL1 not in request and EOL2 not in request:
 	request += connectiontoclient.recv(1024)
print(request.decode())
connectiontoclient.send(response)
connectiontoclient.close()

serversocket.close()
```
