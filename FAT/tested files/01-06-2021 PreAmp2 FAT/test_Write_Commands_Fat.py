import pytest
import socket
import time
import struct
from hamcrest import *
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.settimeout(1)
socket.connect(("10.2.3.1",14601))
sleep_time = 5 #Seconds


########################################################################################
# LDD write commands
# Sending commad b"\x08\x00\x01\x00\x00\x00\x00"
# Sending commad b"\x08\x00\x01\x00\x00\x00\x01"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 7 = LDD Operational status
def test_WHEN_ldd_control_ON_command_is_set_THEN_ldd_control_mode_is_OPERATIONAL():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n standby <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Control <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '1'

# Sending commad b"\x08\x00\x01\x00\x00\x00\x00"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 7 = LDD Operational status STANDBY
def test_WHEN_ldd_control_OFF_command_is_set_THEN_ldd_control_mode_is_STANDBY():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n standby <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '0'

# Sending commad b"\x08\x00\x01\x00\x00\x00\x01"
# Sending commad b"\x09\x00\x01\x00\x00\x00\x00"
# Sending commad b"\x09\x00\x01\x00\x00\x00\x01"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 6 = LDD Trigger status
def test_GIVEN_ldd_control_ON_WHEN_trigger_command_is_set_THEN_trigger_status_is_ON():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Control <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '1'

# Sending commad b"\x09\x00\x01\x00\x00\x00\x00"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 6 = LDD Trigger status 
def test_GIVEN_ldd_control_ON_WHEN_trigger_command_is_OFF_THEN_trigger_status_is_OFF():
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '0'

# Sending commad b"\x09\x00\x01\x00\x00\x00\x01"
# Sending commad b"\x0A\x00\x01\x00\x00\x00\x00"
# Sending commad b"\x0A\x00\x01\x00\x00\x00\x01"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 5 = LDD Channel status
def test_GIVEN_ldd_control_and_trigger_is_ON_WHEN_lld_channel_command_is_set_ON_THEN_channel_status_is_ON():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '1'

# Sending commad b"\x0A\x00\x01\x00\x00\x00\x00"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 5 = LDD Channel status
def test_GIVEN_ldd_control_and_trigger_is_ON_WHEN_lld_channel_command_is_set_OFF_THEN_channel_status_is_OFF():
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '0'

# Sending commad b"\x0C\x00\x04\x00\x00\x00 + [4 bytes of set value]
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 32 - 35 = LDD Bias Current
def test_GIVEN_ldd_prerequsites_are_ON_WHEN_lld_bias_current_command_is_set_THEN_bias_current_is_set_close_to_setting():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    set_value = 0.2
    socket.send(b"\x0C\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value))
    print("\n bias current set <<", socket.recv(10))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n Bias Current <<",struct.unpack("<f", status_data[32:36])[0])
    assert_that(struct.unpack("<f", status_data[32:36])[0], is_(close_to(set_value,0.1)))

# Sending commad b"\x0D\x00\x04\x00\x00\x00 + [4 bytes of set value]"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 8 - 11 = LDD frequency
def test_GIVEN_ldd_prerequsites_are_ON_WHEN_lld_frequency_command_is_set_THEN_frequency_is_set_close_to_setting():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    set_value = 10.0
    socket.send(b"\x0D\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value))
    print("\n LDD Frequency set <<", socket.recv(10))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n LDD Frequency <<",struct.unpack("<f", status_data[8:12])[0])
    assert_that(struct.unpack("<f", status_data[8:12])[0], is_(close_to(set_value,5.0)))

# Sending commad b"\x0E\x00\x04\x00\x00\x00 + [4 bytes of set value]"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 16 - 19 = LDD Pulse Width
def test_GIVEN_ldd_prerequsites_are_ON_WHEN_lld_pulse_width_command_is_set_THEN_pulse_width_is_set_close_to_setting():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    set_value = 202
    socket.send(b"\x0E\x00\x04\x00\x00\x00" +  set_value.to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse width set <<", socket.recv(10))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("status data ", status_data)
    print("pulse width data ", status_data[16:20])
    print("\n Pulse Width <<",int.from_bytes(status_data[16:20], byteorder="little", signed=False))
    assert_that(int.from_bytes(status_data[16:20], byteorder="little", signed=False), is_(close_to(set_value,5)))

# Sending commad b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 0 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_mode_command_is_set_to_SINGLE_THEN_trigger_mode_is_SINGLE():
    trig_mode = '1'
    trig_edge = '1'#default posivitive
    trig_source = '0'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n LDD Trigger Settings <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[0] == '1'

# Sending commad b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 0 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_mode_command_is_set_to_CONTINUES_THEN_trigger_mode_is_CONTINUES():
    trig_mode = '0'
    trig_edge = '1'#default posivitive
    trig_source = '0'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    trigger_settings = int('010',2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00\x02")
    print("\n LDD Trigger Settings <<", socket.recv(7))
    time.sleep(sleep_time*2)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[0] == '0'

# Sending commad b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 1 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_EDGE_command_is_set_to_POSITIVE_THEN_trigger_EDGE_is_POSITIVE():
    trig_mode = '0'
    trig_edge = '1'
    trig_source = '0'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n LDD Trigger Settings <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[1] == '1'

# Sending commad b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 1 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_EDGE_command_is_set_to_NEGATIVE_THEN_trigger_EDGE_is_NEGATIVE():
    trig_mode = '0'
    trig_edge = '0'
    trig_source = '0'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger Settings <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[1] == '0'
    
# Sending commad b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 2 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_SOURCE_command_is_set_to_EXTERNAL_THEN_trigger_SOURCE_is_EXTERNAL():
    trig_mode = '0'
    trig_edge = '1'#default posivitive
    trig_source = '1'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n LDD Trigger Settings <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[2] == '1'

# Sending commad b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 2 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_SOURCE_command_is_set_to_INTERNAL_THEN_trigger_SOURCE_is_INTERNAL():
    trig_mode = '0'
    trig_edge = '1'#default posivitive
    trig_source = '0'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n LDD Trigger Settings <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[2] == '0'


# to run this test and check its working, need to enable any error in laser diode driver
# Sending commad b"\x14\x00\x00\x00\x00\x00"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 0 = LDD Trigger Mode
def test_WHEN_ldd_reset_error_command_IS_issued_all_the_errors_are_RESET():
    socket.send(b"\x13\x00\x00\x00\x00\x00")
    print("\n ldd reset error command on <<", socket.recv(7))
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n LDD error code", status_data[7:8])
    time.sleep(sleep_time*2)
    assert int.from_bytes(status_data[7:8], byteorder="little", signed=False) == 0

####################### soft Start Commands ###########################

# Sending commad b"\x0A\x00\x01\x00\x00\x00\x01"
# Sending commad b"\x0B\x00\x04\x00\x00\x00 + [4 bytes of set value]"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 24 -27 = LDD Pulse Current
def test_GIVEN_ldd_prerequsites_are_ON_and_softstart_is_OFF_WHEN_lld_pulse_current_command_is_set_THEN_pulse_current_is_set_close_to_setting():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", socket.recv(7))
    time.sleep(sleep_time)
    socket.send(b"\x15\x00\x01\x00\x00\x00\x00")
    print("\n LDD Soft Start <<", socket.recv(7))
    time.sleep(sleep_time*3)
    set_value = 10
    socket.send(b"\x0B\x00\x04\x00\x00\x00" + set_value.to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse current set <<", socket.recv(10))
    time.sleep(sleep_time*3)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n Pulse Current <<",int.from_bytes(status_data[24:28], byteorder="little", signed=False))
    assert_that(int.from_bytes(status_data[24:28], byteorder="little", signed=False), is_(close_to(set_value,5)))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '1'
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[1] == '0'
    socket.send(b"\x15\x00\x01\x00\x00\x00\x01")
    print("\n LDD Soft Start <<", socket.recv(7))
    time.sleep(sleep_time*3)



# Sending commad b"\x15\x00\x01\x00\x00\x00 + [1 byte of SoftStart Setting]"
# Sending commad b"\x02\x00\x00\x00\x00\x00"
# Byte 40, Bit 1 = LDD Trigger Mode
def test_GIVEN_ldd_is_Connected_WHEN_ldd_softstart_command_is_set_to_ON_THEN_ldd_status_shows_softstart_ENABLED():
    socket.send(b"\x15\x00\x01\x00\x00\x00\x00")
    print("\n softstart on <<", socket.recv(7))
    time.sleep(sleep_time*3)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[40:41]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[7] == '0'
    socket.send(b"\x15\x00\x01\x00\x00\x00\x01")
    print("\n softstart on <<", socket.recv(7))
    time.sleep(sleep_time*3)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = socket.recv(41)
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[40:41]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[7] == '1'


######################################### Water Chiller write commands ################################################

def test_WHEN_water_chiller_OFF_command_is_set_THEN_chiller_status_is_STANDBY():
    socket.settimeout(1)
    socket.send(b"\x10\x00\x01\x00\x00\x00\x00")
    try:
        time.sleep(12.5)
        print("\n Amplifier error <<", socket.recv(1024))
    except:
        pass
    #print("\n  water chiller status <<", socket.recv(1024))
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >>", b"\x05\x00\x00\x00\x00\x00")
    try:
        status_data = socket.recv(1024)
        print("\n Amplifier error <<", status_data)
    except:
        pass
    try:
        status_data = socket.recv(1024)
    except:
        pass
    print("\n water chiller data <<", status_data)
    print("\n Chiller status <<",bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7])
    assert bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7] == '0'


def test_WHEN_water_chiller_ON_command_is_set_THEN_chiller_status_is_OPERATIONAL():
    socket.send(b"\x10\x00\x01\x00\x00\x00\x01")
    try:
        status_data = socket.recv(1024)
        print("\n Amplifier error <<", status_data)
    except:
        pass
    try:
        print("\n water chiller command on <<", socket.recv(1024))
    except:
        pass
    time.sleep(sleep_time*2)
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >>", b"\x05\x00\x00\x00\x00\x00")
    try:
        status_data = socket.recv(1024)
        print("\n Amplifier error <<", status_data)
    except:
        pass
    try:
        status_data = socket.recv(1024)
    except:
        pass
    print("\n water chiller data <<", status_data)
    print("\n Chiller status <<",bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7])
    assert bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7] == '1'


def test_GIVEN_chiller_is_OPERATIONAL_WHEN_water_chiller_temperature_is_set_THEN_check_if_temperature_is_SET():
    socket.send(b"\x10\x00\x01\x00\x00\x00\x01")
    print("\n water chiller command on <<", socket.recv(1024))
    time.sleep(sleep_time*2)
    set_value = 20.5
    socket.send(b"\x11\x00\x04\x00\x00\x00" + struct.pack("<f", set_value))
    print("\n water chiller water temperature set <<", socket.recv(1024))
    time.sleep(sleep_time*3)
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >>", b"\x05\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n water chiller data <<", status_data)
    set_point_temperature_bytes = status_data[14:18]
    print("\n water chiller status bytes 7-10  <<",struct.unpack("<f", status_data[6:10])[0])
    print("\n water chiller status bytes 11-14 <<",struct.unpack("<f", status_data[10:14])[0])
    print("\n water chiller status bytes 15-18 <<",struct.unpack("<f", status_data[14:18])[0])
    print("\n Chiller temperature <<", struct.unpack("<f", set_point_temperature_bytes)[0])
    assert_that(struct.unpack("<f", set_point_temperature_bytes)[0], is_(close_to(set_value, 10)))
    assert bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7] == '1'


def test_WHEN_chiller_reset_error_command_IS_issued_all_the_errors_are_RESET_and_turn_water_chiller_ON():
    socket.send(b"\x14\x00\x00\x00\x00\x00")
    print("\n water chiller reset set <<", socket.recv(1024))
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >>", b"\x05\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n water chiller data <<", status_data)
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
    time.sleep(sleep_time*2)
    assert (dry_run_error or water_level_warning or low_pressure_error or flow_rate_error or high_temperature_warning or low_temperature_warning or high_temperature_error or low_temperature_error or high_pressure_error) == 0
    socket.send(b"\x10\x00\x01\x00\x00\x00\x01")
    print("\n water chiller command on <<", socket.recv(7))
    time.sleep(sleep_time*2)

#################################### Amplifier Control write commands #####################################################

def test_WHEN_amplifier_OFF_command_is_set_THEN_amplifier_status_is_STANDBY():
    socket.send(b"\x12\x00\x01\x00\x00\x00\x00")
    try:
        print("\n Amplifier control", socket.recv(1024))
    except:
        pass
    try:
        time.sleep(sleep_time*5)
        print("\n Amplifier control", socket.recv(1024))
    except:
        pass
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >>", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data <<", status_data)
    amplifier_control = bin(ord(status_data[31:32]))[2:].rjust(8, '0')
    print("\n Amplifier status <<", amplifier_control[5] , " \n amplifier control << ", amplifier_control )
    assert amplifier_control[5] == '0'


def test_WHEN_amplifier_ON_command_is_set_THEN_amplifier_status_is_OPERATIONAL():
    socket.send(b"\x12\x00\x01\x00\x00\x00\x01")
    try:
        print("\n Amplifier control << ", socket.recv(1024))
    except:
        pass
    try:
        time.sleep(sleep_time*5)
        print("\n Amplifier control", socket.recv(1024))
    except:
        pass
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >>", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(1024)
    print("\n Amplifier data <<", status_data)
    amplifier_control = bin(ord(status_data[31:32]))[2:].rjust(8, '0')
    print("\n Amplifier status <<", amplifier_control[5] , " \n amplifier control << ", amplifier_control )
    assert amplifier_control[5] == '1'
    