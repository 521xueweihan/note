from socket import *

HOST = ''
PORT = 8000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_client_sock = socket(AF_INET, SOCK_STREAM)
tcp_client_sock.connect(ADDR)

while 1:
    send_data = raw_input('input something >')
    if not send_data:
        break
    tcp_client_sock.send(send_data)
    recv_data = tcp_client_sock.recv(BUFSIZ)
    if not recv_data:
        break
    print recv_data
tcp_client_sock.close()
