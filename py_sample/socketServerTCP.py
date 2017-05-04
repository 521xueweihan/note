from SocketServer import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST= ''
PORT = 8000
ADDR = (HOST, PORT)

# 通过继承SocketServer重写handle方法，实现处理请求
# 好处是：只需要调用该类的属性，同时只需要传入参数就可以建立socket通信
class MyRequerstHandler(SRH):
    def handle(self):
        print 'connect from:', self.client_address
        self.wfile.write('[%s]%s' % (ctime(), self.rfile.readline()))

TcpServer = TCP(ADDR, MyRequerstHandler)
print 'waiting for connection'
TcpServer.serve_forever()
