from socket import *

HOST='localhost'
PORT = 8000
BUFSIZ=1024
ADDR = (HOST, PORT)

while 1:
    tcp_client_sock = socket(AF_INET, SOCK_STREAM)
    tcp_client_sock.connect(ADDR)
    data = raw_input(' >')
    if not data:
        break
    # 由于server使用readline()，所以需要换行，否则server不处理传过来的数据
    tcp_client_sock.send('%s\r\n'%data)
    data = tcp_client_sock.recv(BUFSIZ)
    if not data:
        break
    print data
tcp_client_sock.close()
