import pytest
import socket
import time
import struct
from hamcrest import *
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("10.2.3.1",14601))
sleep_short = 2
sleep_time = 5
########################################################################################
# LDD read Commands
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 4 = connection status (LDD)
def test_WHEN_ldd_is_Connected_THEN_get_ldd_command_shows_CONNECTED():
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >> ", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n driver data << ", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    time.sleep(sleep_short)
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[4] == '1'

# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 7 = Error code (LDD)
def test_WHEN_LDD_driver_is_operated_THEN_operational_parameters_are_OK():
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >> ", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n driver data << ", status_data)
    error_code = int.from_bytes(status_data[7:8], byteorder='little')
    print("\n error code <<", error_code)
    time.sleep(sleep_short)
    assert error_code == 0

# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 8 - 11 = Frequency (LDD)
# Byte 12 - 15 = Max Frequency (LDD)
# Byte 16 - 19 = Pulse width (LDD)
# Byte 20 - 23 = Max Pulse width (LDD)
# Byte 24 - 27 = Pulse current (LDD)
# Byte 28 - 31 = Max Pulse current (LDD)
# Byte 32 - 35 = Bias current (LDD)
# Byte 36 - 39 = Max Bias current (LDD)
def test_WHEN_ldd_is_Connected_and_check_Default_values():
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >> ", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n driver data << ", status_data)
    
    print("\n Frequency <<",struct.unpack("<f", status_data[8:12])[0])
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", status_data[8:12])[0], is_(close_to(10.0, 5.0)))
    
    print("\n Maximum Frequency <<",struct.unpack("<f", status_data[12:16])[0])
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", status_data[12:16])[0], is_(close_to(10, 5.0)))
    
    print("\n Pulse Width <<",int.from_bytes(status_data[16:20], byteorder="little", signed=False))
    time.sleep(sleep_short)
    assert_that(int.from_bytes(status_data[16:20], byteorder="little", signed=False), is_(close_to(202, 50)))
    
    print("\n Maximum Pulse Width <<",int.from_bytes(status_data[20:24], byteorder="little", signed=False))
    time.sleep(sleep_short)
    assert_that(int.from_bytes(status_data[20:24], byteorder="little", signed=False), is_(close_to(1500, 10)))
    
    print("\n Pulse Current <<",int.from_bytes(status_data[24:28], byteorder="little", signed=False))
    time.sleep(sleep_short)
    assert_that(int.from_bytes(status_data[24:28], byteorder="little", signed=False), is_(close_to(50, 2)))
    
    print("\n Maximum Pulse Current <<",int.from_bytes(status_data[28:32], byteorder="little", signed=False))
    time.sleep(sleep_short)
    assert_that(int.from_bytes(status_data[28:32], byteorder="little", signed=False), is_(close_to(500, 50)))
    
    print("\n Bias Current <<",struct.unpack("<f", status_data[32:36])[0])
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", status_data[32:36])[0], is_(close_to(0.0, 3.5)))
    
    print("\n Maximum Bias Current <<",struct.unpack("<f", status_data[36:40])[0])
    time.sleep(sleep_time*2)
    assert_that(struct.unpack("<f", status_data[36:40])[0], is_(close_to(1.0, 0.5)))


########################################################################################
# Water chiller read Commands

    
# Sending commad b"\x05\x00\x00\x00\x00\x00"
# Byte 20, Bit 0 = Chiller connection status
def test_WHEN_Water_Chiller_is_Connected_THEN_get_water_chiller_data_command_shows_CONNECTED():
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >> ", b"\x05\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n water chiller data << ", status_data)
    chiller_status = bin(ord(status_data[20:21]))[2:]
    print("\n status <<", chiller_status)
    time.sleep(sleep_short)
    assert chiller_status[0] == '1'

# Sending commad b"\x05\x00\x00\x00\x00\x00"
# Byte 19 = Chiller errors
def test_WHEN_WATER_CHILLER_is_operated_THEN_operational_parameters_are_OK():
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >> ", b"\x05\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n water chiller data << ", status_data)
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
    time.sleep(sleep_short)
    assert (dry_run_error or water_level_warning or low_pressure_error or flow_rate_error or high_temperature_warning or low_temperature_warning or high_temperature_error or low_temperature_error or high_pressure_error) == 0

# Sending commad b"\x05\x00\x00\x00\x00\x00"
# Byte 10-13 = water flow rate
def test_WATER_CHILLER_WATER_FLOW_RATE_is_within_limits():
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >> ", b"\x05\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n water chiller data << ", status_data)
    water_flow = struct.unpack("<f", status_data[10:14])[0]
    print("water flow rate in water chiller is ", water_flow)
    time.sleep(sleep_short)
    assert_that(water_flow, is_(close_to(5.8, 1.0)))

# Sending commad b"\x05\x00\x00\x00\x00\x00"
# Byte 6 - 9 = water temperature
def test_WATER_CHILLER_WATER_TEMPERATURE_is_within_limits():
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >> ", b"\x05\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n water chiller data << ", status_data)
    water_temperature = struct.unpack("<f", status_data[6:10])[0]
    print("water temperature in water chiller is ", water_temperature)
    time.sleep(sleep_time*2)
    assert_that(water_temperature, is_(close_to(20.0,5.0)))

########################################################################################
# Amplifier Read commands

# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 31, Bit 4 = Amplifier connection status
def test_WHEN_amplifier_is_Connected_THEN_get_amplifier_command_shows_CONNECTED():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data << ", status_data)
    print("\n Amplifier status <<",bin(ord(status_data[31:32]))[2:].rjust(8, '0'))
    time.sleep(sleep_short)
    assert bin(ord(status_data[31:32]))[2:].rjust(8, '0')[4] == '0'

# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 7-10 = Amplifier humidity (PM)
def test_GIVEN_amplifier_is_connected_THEN_pump_relative_humidity_is_close_to_setting():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data << ", status_data)
    pm_rel_humidity = status_data[6:10]
    print("\n Pump Relative humidity <<", pm_rel_humidity)
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", pm_rel_humidity)[0], is_(close_to(22.5, 22.5)))
    
# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 11-14 = PM flow rate
def test_GIVEN_amplifier_is_connected_THEN_pump_waterflow_rate_is_close_to_setting():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data << ", status_data)
    pm_waterflow_rate = status_data[10:14]
    print("\n Pump water flow rate <<", pm_waterflow_rate)
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", pm_waterflow_rate)[0], is_(close_to(0.3, 1.0)))
    
# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 15-18 = Pump ambient temperature
def test_GIVEN_amplifier_is_connected_THEN_pump_ambient_temperature_is_close_to_setting():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data << ", status_data)
    pm_ambient_temp = status_data[14:18]
    print("\n Pump ambient temp <<", pm_ambient_temp)
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", pm_ambient_temp)[0], is_(close_to(22.5, 5.0)))
    
# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 19-22 = Pump heatsink temperature
def test_GIVEN_amplifier_is_connected_THEN_pump_heat_sink_temperature_is_close_to_setting():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data << ", status_data)
    pm_heat_sink_temp = status_data[18:22]
    print("\n Pump heat sink temp <<", pm_heat_sink_temp)
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", pm_heat_sink_temp)[0], is_(close_to(21.5, 5.0)))
    
# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 23-26 = V.chamber pressure
def test_GIVEN_amplifier_is_connected_THEN_amplifier_vacuum_pressure_is_close_to_setting():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data << ", status_data)
    vacuum_pressure = status_data[22:26]
    print("\n Vacuum pressure <<", vacuum_pressure)
    time.sleep(sleep_short)
#    assert_that(struct.unpack("<f", vacuum_pressure)[0], is_(close_to(1000.0, 20.0)))
    assert_that(struct.unpack("<f", vacuum_pressure)[0], is_(close_to(20.0, 20.0)))

# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 27-30 = Crystal temperature
def test_GIVEN_amplifier_is_connected_THEN_crystal_temperature_is_close_to_setting():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data << ", status_data)
    crystal_temperature = status_data[26:30]
    print("\n Crystal temperature <<", crystal_temperature)
    time.sleep(sleep_short)
#    assert_that(struct.unpack("<f", crystal_temperature)[0], is_(close_to(20.0, 5.0)))
    assert_that(struct.unpack("<f", crystal_temperature)[0], is_(close_to(-20.0, 5.0)))
    
# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 30 = Error
def test_GIVEN_amplifier_is_connected_THEN_all_pump_parameters_are_OK():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data << ", status_data)
    error_bits = bin(ord(status_data[30:31]))[2:].rjust(8, '0')
    print("Pump errors <<", error_bits)
    emergency_stop_error = int(error_bits[0])
    door_error = int(error_bits[1])
    water_chiller_error = int(error_bits[2])
    enclosure_error = int(error_bits[3])
    pm_heat_sink_temp_error = int(error_bits[4])
    pm_ambient_temp_error = int(error_bits[5])
    pm_rel_humidity_temp_error = int(error_bits[6])
    pm_water_flow_error = int(error_bits[7])
    time.sleep(sleep_short)
    assert (emergency_stop_error or door_error or water_chiller_error or enclosure_error or pm_heat_sink_temp_error or pm_ambient_temp_error or pm_rel_humidity_temp_error or pm_water_flow_error) == 0
    
# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 31 = Error
def test_GIVEN_amplifier_is_connected_THEN_all_amplifier_parameters_are_OK():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data << ", status_data)
    error_bits = bin(ord(status_data[31:32]))[2:].rjust(8, '0')
    print("Amplifier errors <<", error_bits)
    crystal_temp_error = int(error_bits[7])
    vacuum_pressure_error = int(error_bits[6])
    time.sleep(sleep_time*3)
    assert (crystal_temp_error or vacuum_pressure_error) == 0
