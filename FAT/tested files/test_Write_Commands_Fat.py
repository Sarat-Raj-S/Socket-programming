import pytest
import socket
import time
import struct
from hamcrest import *
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("10.2.3.1",14601))
sleep_time = 2 #Seconds

########################################################################################
# Water Chiller write commands

def test_WHEN_water_chiller_OFF_command_is_set_THEN_chiller_status_is_STANDBY():
    print("Sent Chiller off command")
    socket.send(b"\x10\x00\x01\x00\x00\x00\x00")
    ack = socket.recv(7)
    time.sleep(sleep_time*14)
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    status = socket.recv(21)
    time.sleep(sleep_time)
    print("\n Chiller status <<",bin(ord(status[18:19]))[2:].rjust(8,'0'))
    assert bin(ord(status[18:19]))[2:].rjust(8,'0')[7] == '0'

def test_WHEN_water_chiller_ON_command_is_set_THEN_chiller_status_is_OPERATIONAL():
    print("Sent Chiller on command")
    socket.send(b"\x10\x00\x01\x00\x00\x00\x01")
    ack = socket.recv(7)
    time.sleep(sleep_time*10)
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    status = socket.recv(21)
    time.sleep(sleep_time)
    print("\n Chiller status <<",bin(ord(status[18:19]))[2:].rjust(8,'0'))
    assert bin(ord(status[18:19]))[2:].rjust(8,'0')[7] == '1'

def test_GIVEN_chiller_is_connected_WHEN_water_chiller_temperature_is_set_THEN_check_if_temperature_is_SET():
    print("Sent Chiller set point temp command")
    set_point_bytes = struct.pack("<f", 20.0)
    print("set_point_bytes",set_point_bytes)
    socket.send(b"\x11\x00\x04\x00\x00\x00"+set_point_bytes )
    ack = socket.recv(10)
    # print("Ack:", ack)
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    status = socket.recv(21)
    time.sleep(sleep_time)
    set_point_temperature_bytes = status[14:18]
    print("\n 7-10 ",struct.unpack("<f", status[6:10])[0])
    print("\n 11-14 ",struct.unpack("<f", status[10:14])[0])
    print("\n 15-18 ",struct.unpack("<f", status[14:18])[0])
    print("\n Chiller temperature <<",struct.unpack("<f", status[14:18])[0])
    assert_that(struct.unpack("<f", set_point_temperature_bytes)[0], is_(close_to(20, 3)))

def test_WHEN_chiller_reset_error_command_IS_issued_all_the_errors_are_RESET():
    print("Sent Chiller reset error command")
    socket.send(b"\x14\x00\x00\x00\x00\x00")
    ack = socket.recv(8)
    # print("\n Chiller error Acknowledge", ack)
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    status_data = socket.recv(21)
    print("\n Chiller error code", status_data[19:21])
    error_bits_of_byte1 = bin(ord(status_data[19:20]))[2:].rjust(8, '0')
    error_bits_of_byte2 = bin(ord(status_data[20:21]))[2:].rjust(8, '0')
    print("\n error <<", error_bits_of_byte1, error_bits_of_byte2)
    dry_run_error = int(error_bits_of_byte1[0])
    water_level_warning = int(error_bits_of_byte1[1])
    low_pressure_error = int(error_bits_of_byte1[2])
    flow_rate_error = int(error_bits_of_byte1[3])
    high_temperature_warning = int(error_bits_of_byte1[4])
    low_temperature_warning = int(error_bits_of_byte1[5])
    high_temperature_error = int(error_bits_of_byte1[6])
    low_temperature_error = int(error_bits_of_byte1[7])
    high_pressure_error = int(error_bits_of_byte2[7])
    time.sleep(sleep_time)
    assert (dry_run_error or water_level_warning or low_pressure_error or flow_rate_error or high_temperature_warning or low_temperature_warning or high_temperature_error or low_temperature_error or high_pressure_error) == 0

'''
########################################################################################
# Amplifier Control write commands

def test_WHEN_amplifier_OFF_command_is_set_THEN_amplifier_status_is_STANDBY():
    print("Sent Amplifier control off command")
    socket.send(b"\x12\x00\x01\x00\x00\x00\x00")
    ack = socket.recv(7)
    time.sleep(sleep_time)
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    status = socket.recv(32)
    amplifier_control = bin(ord(status[31:32]))[2:].rjust(8, '0')
    print("\n Amplifier status <<", amplifier_control[5])
    assert amplifier_control[0] == '1'
#   We look for shutdown mode here

def test_WHEN_amplifier_ON_command_is_set_THEN_amplifier_status_is_OPERATIONAL():
    print("Sent Amplifier control on command")
    socket.send(b"\x12\x00\x01\x00\x00\x00\x01")
    ack = socket.recv(7)
    time.sleep(sleep_time)
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    status = socket.recv(32)
    amplifier_control = bin(ord(status[31:32]))[2:].rjust(8, '0')
    print("\n Amplifier status <<", amplifier_control[5])
    assert amplifier_control[5] == '1'
'''