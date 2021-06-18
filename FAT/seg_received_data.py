# import pytest
# import socket
# import time
# import struct
# from hamcrest import *
# socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.settimeout(1)
# socket.connect(("10.2.3.1",14601))
# sleep_time = 5 #Seconds
# socket.send(b"\x02\x00\x00\x00\x00\x00")
# buff_data = receive()
# seg_data(buff_data)

# def receive():
#     buff_data = socket.recv(1)
#     while True:
#         try:
#             buff_data += socket.recv(1)
#         except:
#             print("Completed Reading data : ", buff_data)
#             break
#     return buff_data


# def seg_data(buff_data):
#     print("received data is :"buff_data)