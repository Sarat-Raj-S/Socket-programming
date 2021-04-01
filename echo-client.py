#!/usr/bin/env python3

import socket
from data import *

#s = socket.socket()
#s.connect(('127.0.0.1',65432))
i=0
print(i)
#print(vi.encode())
#s.sendall(vi.encode())
#image_data = s.recv(3000000)
image_data = vi#.encode()
image_data_output = image_data[6:]
length_of_image_data_1D = len(image_data_output)
print("length is:",length_of_image_data_1D)
#s.close()