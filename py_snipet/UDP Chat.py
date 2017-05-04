#!/usr/bin/env python
# source: https://thecodeninja.net/category/python/
import socket
import sys, select

# Read a line. Using select for non blocking reading of sys.stdin
def getLine():
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
            return input
    return False

host = raw_input("Please Enter IP: ")
port = int(raw_input("Please Enter PORT: "), 16) # Base 16 for hex value

send_address = (host, port) # Set the address to send to
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # Create Datagram Socket (UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Make Socket Reusable
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Allow incoming broadcasts
s.setblocking(False) # Set socket to non-blocking mode
s.bind(('', port)) #Accept Connections on port
print "Accepting connections on port", hex(port)

while 1:
    try:
        message, address = s.recvfrom(8192) # Buffer size is 8192. Change as needed.
        if message:
            print address, "> ", message
    except:
        pass

    input = getLine();
    if(input != False):
        s.sendto(input, send_address)
