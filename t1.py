#!/usr/bin/env python2
from socket import *
import sys

host=sys.argv[1]
port=199

data = file('1.bin','rb').read()
sock=socket(AF_INET,SOCK_STREAM)
sock.connect((host,port))
sock.sendall(data)
print list(sock.recv(10000))
sock.close()
print 'sent'


