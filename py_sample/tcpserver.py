from socket import *
from time import ctime


HOST= ''
PORT=8000
BUFSIZ=1024
ADDR = (HOST, PORT)

tcp_server_sock = socket(AF_INET, SOCK_STREAM)
tcp_server_sock.bind(ADDR)
tcp_server_sock.listen(5)

while 1:
    print 'waiting for connection...'
    tcp_client_sock, addr = tcp_server_sock.accept()
    print 'connecting from:', addr
    
    while 1:
        data = tcp_client_sock.recv(BUFSIZ)
        if not data:
            break
        tcp_client_sock.send('[%s]:%s' % (ctime(), data))
tcp_server_sock.close()
