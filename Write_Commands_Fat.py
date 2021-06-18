import pytest
import socket
import time
import struct
from hamcrest import *
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.settimeout(1)
socket.connect(("127.0.0.1",9999))
sleep_time = 5 #Seconds

def receive(byte_check, command):
    status_data = socket.recv(1024)
    while True:
        if status_data[0:1] == byte_check:
            break
        else:
            socket.send(command)
            print("\n sending command >>", command)
            status_data = socket.recv(1024)
    return status_data

########################################################################################
# LDD write commands
# Sending command b"\x08\x00\x01\x00\x00\x00\x00"
# Sending command b"\x08\x00\x01\x00\x00\x00\x01"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 7 = LDD Operational status
def test_WHEN_ldd_control_ON_command_is_set_THEN_ldd_control_mode_is_OPERATIONAL():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n LDD Control <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Control <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '1'


# Sending command b"\x08\x00\x01\x00\x00\x00\x00"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 7 = LDD Operational status STANDBY
def test_WHEN_ldd_control_OFF_command_is_set_THEN_ldd_control_mode_is_STANDBY():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n LDD Control <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '0'

# Sending command b"\x08\x00\x01\x00\x00\x00\x01"
# Sending command b"\x09\x00\x01\x00\x00\x00\x00"
# Sending command b"\x09\x00\x01\x00\x00\x00\x01"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 6 = LDD Trigger status
def test_GIVEN_ldd_control_ON_WHEN_trigger_command_is_set_THEN_trigger_status_is_ON():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Control <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09",b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '1'

# Sending command b"\x09\x00\x01\x00\x00\x00\x00"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 6 = LDD Trigger status 
def test_GIVEN_ldd_control_ON_WHEN_trigger_command_is_OFF_THEN_trigger_status_is_OFF():
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '0'

# Sending command b"\x09\x00\x01\x00\x00\x00\x01"
# Sending command b"\x0A\x00\x01\x00\x00\x00\x00"
# Sending command b"\x0A\x00\x01\x00\x00\x00\x01"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 5 = LDD Channel status
def test_GIVEN_ldd_control_and_trigger_is_ON_WHEN_lld_channel_command_is_set_ON_THEN_channel_status_is_ON():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '1'

# Sending command b"\x0A\x00\x01\x00\x00\x00\x00"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 5 = LDD Channel status
def test_GIVEN_ldd_control_and_trigger_is_ON_WHEN_lld_channel_command_is_set_OFF_THEN_channel_status_is_OFF():
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '0'


# Sending command b"\x0C\x00\x04\x00\x00\x00 + [4 bytes of set value]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 32 - 35 = LDD Bias Current
def test_GIVEN_ldd_prerequsites_are_ON_WHEN_lld_bias_current_command_is_set_THEN_bias_current_is_set_close_to_setting():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    set_value = 0.6
    socket.send(b"\x0C\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value))
    print("\n bias current set <<", receive(b"\x0C", b"\x0C\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value)))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n Bias Current <<",struct.unpack("<f", status_data[32:36])[0])
    assert_that(struct.unpack("<f", status_data[32:36])[0], is_(close_to(set_value,1.0)))

# Sending command b"\x0D\x00\x04\x00\x00\x00 + [4 bytes of set value]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 8 - 11 = LDD frequency
def test_GIVEN_ldd_prerequsites_are_ON_WHEN_lld_frequency_command_is_set_THEN_frequency_is_set_close_to_setting():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    set_value = 10.0
    socket.send(b"\x0D\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value))
    print("\n LDD Frequency set <<", receive(b"\x0D", b"\x0D\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value)))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n LDD Frequency <<",struct.unpack("<f", status_data[8:12])[0])
    assert_that(struct.unpack("<f", status_data[8:12])[0], is_(close_to(set_value,5.0)))

# Sending command b"\x0E\x00\x04\x00\x00\x00 + [4 bytes of set value]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 16 - 19 = LDD Pulse Width
def test_GIVEN_ldd_prerequsites_are_ON_WHEN_lld_pulse_width_command_is_set_THEN_pulse_width_is_set_close_to_setting():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    set_value = 202
    socket.send(b"\x0E\x00\x04\x00\x00\x00" +  set_value.to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse width set <<", receive(b"\x0E", b"\x0E\x00\x04\x00\x00\x00" +  set_value.to_bytes(length=4, byteorder="little", signed=False)))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("status data ", status_data)
    print("pulse width data ", status_data[16:20])
    print("\n Pulse Width <<",int.from_bytes(status_data[16:20], byteorder="little", signed=False))
    assert_that(int.from_bytes(status_data[16:20], byteorder="little", signed=False), is_(close_to(set_value,5)))

# Sending command b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 0 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_mode_command_is_set_to_SINGLE_THEN_trigger_mode_is_SINGLE():
    trig_mode = '1'
    trig_edge = '1'#default posivitive
    trig_source = '0'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n LDD Trigger Settings <<", receive(b"\x0F", b"\x0F\x00\x01\x00\x00\x00"+trigger_settings))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[0] == '1'

# Sending command b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 0 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_mode_command_is_set_to_CONTINUES_THEN_trigger_mode_is_CONTINUES():
    trig_mode = '0'
    trig_edge = '1'#default posivitive
    trig_source = '0'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n LDD Trigger Settings <<", receive(b"\x0F", b"\x0F\x00\x01\x00\x00\x00"+trigger_settings))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[0] == '0'

# Sending command b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 1 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_EDGE_command_is_set_to_POSITIVE_THEN_trigger_EDGE_is_POSITIVE():
    trig_mode = '0'
    trig_edge = '1'
    trig_source = '0'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n LDD Trigger Settings <<", receive(b"\x0F", b"\x0F\x00\x01\x00\x00\x00"+trigger_settings))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[1] == '1'

# Sending command b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 1 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_EDGE_command_is_set_to_NEGATIVE_THEN_trigger_EDGE_is_NEGATIVE():
    trig_mode = '0'
    trig_edge = '0'
    trig_source = '0'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n LDD Trigger Settings <<", receive(b"\x0F", b"\x0F\x00\x01\x00\x00\x00"+trigger_settings))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[1] == '0'
    
# Sending command b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 2 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_SOURCE_command_is_set_to_EXTERNAL_THEN_trigger_SOURCE_is_EXTERNAL():
    trig_mode = '0'
    trig_edge = '1'#default posivitive
    trig_source = '1'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n LDD Trigger Settings <<", receive(b"\x0F", b"\x0F\x00\x01\x00\x00\x00"+trigger_settings))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[2] == '1'

# Sending command b"\x0F\x00\x01\x00\x00\x00 + [1 byte of Trigger setting]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 2 = LDD Trigger Mode
def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_SOURCE_command_is_set_to_INTERNAL_THEN_trigger_SOURCE_is_INTERNAL():
    trig_mode = '0'
    trig_edge = '1'#default posivitive
    trig_source = '0'
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n LDD Trigger Settings <<", receive(b"\x0F", b"\x0F\x00\x01\x00\x00\x00"+trigger_settings))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[2] == '0'

# to run this test and check its working, need to enable any error in laser diode driver
# Sending command b"\x14\x00\x00\x00\x00\x00"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 0 = LDD Trigger Mode
def test_WHEN_ldd_reset_error_command_IS_issued_all_the_errors_are_RESET():
    socket.send(b"\x13\x00\x00\x00\x00\x00")
    print("\n ldd reset error command on <<", receive(b"\x13", b"\x13\x00\x00\x00\x00\x00"))
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n LDD error code", status_data[7:8])
    assert int.from_bytes(status_data[7:8], byteorder="little", signed=False) == 0

######################################### Water Chiller write commands ################################################


def test_WHEN_water_chiller_ON_command_is_set_THEN_chiller_status_is_OPERATIONAL():

    socket.send(b"\x10\x00\x01\x00\x00\x00\x00")
    print("\n water chiller command off <<", receive(b"\x10", b"\x10\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x10\x00\x01\x00\x00\x00\x01")
    print("\n water chiller command on <<", receive(b"\x10", b"\x10\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >>", b"\x05\x00\x00\x00\x00\x00")
    status_data = receive(b"\x05", b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data <<", status_data)
    print("\n Chiller status <<",bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7])
    assert bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7] == '1'


def test_WHEN_water_chiller_OFF_command_is_set_THEN_chiller_status_is_STANDBY():
    socket.send(b"\x10\x00\x01\x00\x00\x00\x00")
    print("\n water chiller command off <<", receive(b"\x10", b"\x10\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >>", b"\x05\x00\x00\x00\x00\x00")
    status_data = receive(b"\x05", b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data <<", status_data)
    print("\n Chiller status <<",bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7])
    assert bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7] == '0'


def test_GIVEN_chiller_is_OPERATIONAL_WHEN_water_chiller_temperature_is_set_THEN_check_if_temperature_is_SET():
    socket.send(b"\x10\x00\x01\x00\x00\x00\x01")
    print("\n water chiller command on <<", receive(b"\x10", b"\x10\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    set_value = 18.0
    socket.send(b"\x11\x00\x04\x00\x00\x00" + struct.pack("<f", set_value))
    print("\n water chiller water temperature set <<", receive(b"\x11", b"\x11\x00\x04\x00\x00\x00" + struct.pack("<f", set_value)))
    time.sleep(sleep_time*3)
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >>", b"\x05\x00\x00\x00\x00\x00")
    status_data = receive(b"\x05", b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data <<", status_data)
    set_point_temperature_bytes = status_data[14:18]
    print("\n water chiller status bytes 7-10  <<",struct.unpack("<f", status_data[6:10])[0])
    print("\n water chiller status bytes 11-14 <<",struct.unpack("<f", status_data[10:14])[0])
    print("\n water chiller status bytes 15-18 <<",struct.unpack("<f", status_data[14:18])[0])
    print("\n Chiller temperature <<", struct.unpack("<f", set_point_temperature_bytes)[0])
    assert_that(struct.unpack("<f", set_point_temperature_bytes)[0], is_(close_to(set_value, 10)))
    assert bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7] == '1'


def test_GIVEN_chiller_is_STANDBY_WHEN_water_chiller_temperature_is_set_THEN_check_if_temperature_is_SET():
    socket.send(b"\x10\x00\x01\x00\x00\x00\x00")
    print("\n water chiller command off <<", receive(b"\x10", b"\x10\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    set_value = 30.0
    socket.send(b"\x11\x00\x04\x00\x00\x00" + struct.pack("<f", set_value))
    print("\n water chiller water temperature set <<", receive(b"\x11", b"\x11\x00\x04\x00\x00\x00" + struct.pack("<f", set_value)))
    time.sleep(sleep_time*3)
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >>", b"\x05\x00\x00\x00\x00\x00")
    status_data = receive(b"\x05", b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data <<", status_data)
    set_point_temperature_bytes = status_data[14:18]
    print("\n Chiller temperature <<", struct.unpack("<f", set_point_temperature_bytes)[0])
    assert_that(struct.unpack("<f", set_point_temperature_bytes)[0], is_(close_to(set_value, 5)))
    assert bin(ord(status_data[18:19]))[2:].rjust(8, '0')[7] == '0'


def test_WHEN_chiller_reset_error_command_IS_issued_all_the_errors_are_RESET():
    socket.send(b"\x14\x00\x00\x00\x00\x00")
    print("\n water chiller reset set <<", receive(b"\x14", b"\x14\x00\x00\x00\x00\x00"))
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >>", b"\x05\x00\x00\x00\x00\x00")
    status_data = receive(b"\x05", b"\x05\x00\x00\x00\x00\x00")
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
    time.sleep(sleep_time)
    assert (dry_run_error or water_level_warning or low_pressure_error or flow_rate_error or high_temperature_warning or low_temperature_warning or high_temperature_error or low_temperature_error or high_pressure_error) == 0


#################################### Amplifier Control write commands #####################################################


def test_WHEN_amplifier_ON_command_is_set_THEN_amplifier_status_is_OPERATIONAL():
    socket.send(b"\x12\x00\x01\x00\x00\x00\x00")
    print("\n Amplifier control << ", receive(b"\x12", b"\x12\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x12\x00\x01\x00\x00\x00\x01")
    print("\n Amplifier control", receive(b"\x12", b"\x12\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >>", b"\x04\x00\x00\x00\x00\x00")
    status_data = receive(b"\x04", b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data <<", status_data)
    amplifier_control = bin(ord(status_data[31:32]))[2:].rjust(8, '0')
    print("\n Amplifier status <<", amplifier_control[5] , " \n amplifier control << ", amplifier_control )
    assert amplifier_control[5] == '1'


def test_WHEN_amplifier_OFF_command_is_set_THEN_amplifier_status_is_STANDBY():
    socket.send(b"\x12\x00\x01\x00\x00\x00\x00")
    print("\n Amplifier control << ", receive(b"\x12", b"\x12\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >>", b"\x04\x00\x00\x00\x00\x00")
    status_data = receive(b"\x04", b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data <<", status_data)
    amplifier_control = bin(ord(status_data[31:32]))[2:].rjust(8, '0')
    print("\n Amplifier status <<", amplifier_control[5] , " \n amplifier control << ", amplifier_control )
    assert amplifier_control[5] == '0'


######################################### Read Command tests #########################################


sleep_short = 0.2

####################################### LDD read Commands ##################################################

# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 4 = connection status (LDD)
def test_WHEN_ldd_is_Connected_THEN_get_ldd_command_shows_CONNECTED():
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >> ", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data << ", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    time.sleep(sleep_short)
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[4] == '1'

# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 7 = Error code (LDD)
def test_WHEN_LDD_driver_is_operated_THEN_operational_parameters_are_OK():
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >> ", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
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
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data << ", status_data)
    
    print("\n Frequency <<",struct.unpack("<f", status_data[8:12])[0])
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", status_data[8:12])[0], is_(close_to(10.0, 5.0)))
    
    print("\n Maximum Frequency <<",struct.unpack("<f", status_data[12:16])[0])
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", status_data[12:16])[0], is_(close_to(10, 5.0)))
    
    print("\n Pulse Width <<",int.from_bytes(status_data[16:20], byteorder="little", signed=False))
    time.sleep(sleep_short)
    assert_that(int.from_bytes(status_data[16:20], byteorder="little", signed=False), is_(close_to(500, 300)))
    
    print("\n Maximum Pulse Width <<",int.from_bytes(status_data[20:24], byteorder="little", signed=False))
    time.sleep(sleep_short)
    assert_that(int.from_bytes(status_data[20:24], byteorder="little", signed=False), is_(close_to(1500, 10)))
    
    print("\n Pulse Current <<",int.from_bytes(status_data[24:28], byteorder="little", signed=False))
    time.sleep(sleep_short)
    assert_that(int.from_bytes(status_data[24:28], byteorder="little", signed=False), is_(close_to(225, 225)))
    
    print("\n Maximum Pulse Current <<",int.from_bytes(status_data[28:32], byteorder="little", signed=False))
    time.sleep(sleep_short)
    assert_that(int.from_bytes(status_data[28:32], byteorder="little", signed=False), is_(close_to(500, 50)))
    
    print("\n Bias Current <<",struct.unpack("<f", status_data[32:36])[0])
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", status_data[32:36])[0], is_(close_to(0.0, 3.5)))
    
    print("\n Maximum Bias Current <<",struct.unpack("<f", status_data[36:40])[0])
    time.sleep(sleep_short)
    assert_that(struct.unpack("<f", status_data[36:40])[0], is_(close_to(1.0, 0.5)))


######################################## Water chiller read Commands #################################################


    
# Sending commad b"\x05\x00\x00\x00\x00\x00"
# Byte 20, Bit 0 = Chiller connection status
def test_WHEN_Water_Chiller_is_Connected_THEN_get_water_chiller_data_command_shows_CONNECTED():
    socket.send(b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data >> ", b"\x05\x00\x00\x00\x00\x00")
    status_data = receive(b"\x05", b"\x05\x00\x00\x00\x00\x00")
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
    status_data = receive(b"\x05", b"\x05\x00\x00\x00\x00\x00")
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
    status_data = receive(b"\x05", b"\x05\x00\x00\x00\x00\x00")
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
    status_data = receive(b"\x05", b"\x05\x00\x00\x00\x00\x00")
    print("\n water chiller data << ", status_data)
    water_temperature = struct.unpack("<f", status_data[6:10])[0]
    print("water temperature in water chiller is ", water_temperature)
    time.sleep(sleep_short)
    assert_that(water_temperature, is_(close_to(20.0,5.0)))

################################### Amplifier Read commands ######################################################


# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 31, Bit 4 = Amplifier connection status
def test_WHEN_amplifier_is_Connected_THEN_get_amplifier_command_shows_CONNECTED():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(b"\x04", b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data << ", status_data)
    print("\n Amplifier status <<",bin(ord(status_data[31:32]))[2:].rjust(8, '0'))
    time.sleep(sleep_short)
    assert bin(ord(status_data[31:32]))[2:].rjust(8, '0')[4] == '0'

# Sending commad b"\x04\x00\x00\x00\x00\x00"
# Byte 7-10 = Amplifier humidity (PM)
def test_GIVEN_amplifier_is_connected_THEN_pump_relative_humidity_is_close_to_setting():
    socket.send(b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data >> ", b"\x04\x00\x00\x00\x00\x00")
    status_data = socket.recv(b"\x04", b"\x04\x00\x00\x00\x00\x00")
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
    status_data = socket.recv(b"\x04", b"\x04\x00\x00\x00\x00\x00")
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
    status_data = socket.recv(b"\x04", b"\x04\x00\x00\x00\x00\x00")
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
    status_data = socket.recv(b"\x04", b"\x04\x00\x00\x00\x00\x00")
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
    status_data = socket.recv(b"\x04", b"\x04\x00\x00\x00\x00\x00")
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
    status_data = socket.recv(b"\x04", b"\x04\x00\x00\x00\x00\x00")
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
    status_data = socket.recv(b"\x04", b"\x04\x00\x00\x00\x00\x00")
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
    status_data = socket.recv(b"\x04", b"\x04\x00\x00\x00\x00\x00")
    print("\n Amplifier data << ", status_data)
    error_bits = bin(ord(status_data[31:32]))[2:].rjust(8, '0')
    print("Amplifier errors <<", error_bits)
    crystal_temp_error = int(error_bits[7])
    vacuum_pressure_error = int(error_bits[6])
    time.sleep(sleep_short)
    assert (crystal_temp_error or vacuum_pressure_error) == 0


######################################### Softstart tests #########################################


# Sending command b"\x15\x00\x01\x00\x00\x00 + [1 byte of SoftStart Setting]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 40, Bit 1 = LDD Trigger Mode
def test_GIVEN_ldd_is_Connected_WHEN_ldd_softstart_command_is_set_to_ON_THEN_ldd_status_shows_softstart_ENABLED():
    socket.send(b"\x15\x00\x01\x00\x00\x00\x01")
    print("\n softstart on <<", receive(b"\x15", b"\x15\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time * 6)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[40:41]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[7] == '1'
    socket.send(b"\x15\x00\x01\x00\x00\x00\x00")
    print("\n softstart off <<", receive(b"\x15", b"\x15\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time * 6)


# Sending command b"\x0A\x00\x01\x00\x00\x00\x01"
# Sending command b"\x0B\x00\x04\x00\x00\x00 + [4 bytes of set value]"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 24 -27 = LDD Pulse Current
def test_GIVEN_ldd_prerequsites_are_ON_and_softstart_is_OFF_WHEN_lld_pulse_current_command_is_set_THEN_pulse_current_is_set_close_to_setting():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x15\x00\x01\x00\x00\x00\x00")
    print("\n LDD Soft Start <<", receive(b"\x15",b"\x15\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time*6)
    set_value = 10
    socket.send(b"\x0B\x00\x04\x00\x00\x00" + set_value.to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse current set <<", receive(b"\x0B", b"\x0B\x00\x04\x00\x00\x00" + set_value.to_bytes(length=4, byteorder="little", signed=False)))
    time.sleep(sleep_time*6)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n Pulse Current <<",int.from_bytes(status_data[24:28], byteorder="little", signed=False))
    assert_that(int.from_bytes(status_data[24:28], byteorder="little", signed=False), is_(close_to(set_value,5)))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '1'
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[1] == '0'
    socket.send(b"\x15\x00\x01\x00\x00\x00\x00")
    print("\n LDD Soft Start <<", receive(b"\x15", b"\x15\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time*6)

######################################### negative tests #########################################

# Sending command b"\x08\x00\x01\x00\x00\x00\x00"
# Sending command b"\x09\x00\x01\x00\x00\x00\x00"
# Sending command b"\x09\x00\x01\x00\x00\x00\x01"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 6 = LDD Trigger status
def test_GIVEN_ldd_control_OFF_WHEN_trigger_command_is_set_THEN_trigger_status_is_NOT_ON():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger<<", receive(b"\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n standby <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x00"))
    print("\n LDD Control <<", receive(b"\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] != '1'


# Sending command b"\x08\x00\x01\x00\x00\x00\x00"
# Sending command b"\x09\x00\x01\x00\x00\x00\x00"
# Sending command b"\x09\x00\x01\x00\x00\x00\x01"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 6 = LDD Trigger status
def test_GIVEN_ldd_control_and_trigger_are_ON_WHEN_ldd_control_command_is_set_to_STANDBY_THEN_trigger_status_is_NOT_ON():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Control <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger<<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n standby <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x00"))
    print("\n LDD Control <<", receive(b"\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] != '1'
    
# Sending command b"\x09\x00\x01\x00\x00\x00\x00"
# Sending command b"\x0A\x00\x01\x00\x00\x00\x00"
# Sending command b"\x0A\x00\x01\x00\x00\x00\x01"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 5 = LDD Channel status
def test_GIVEN_ldd_control_and_trigger_is_OFF_WHEN_lld_channel_command_is_set_to_ON_THEN_channel_status_is_NOT_ON():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger<<", receive(b"\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n standby <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x00"))
    print("\n LDD Control <<", receive(b"\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] != '1'

# Sending command b"\x08\x00\x01\x00\x00\x00\x1"
# Sending command b"\x09\x00\x01\x00\x00\x00\x00"
# Sending command b"\x0A\x00\x01\x00\x00\x00\x00"
# Sending command b"\x0A\x00\x01\x00\x00\x00\x01"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 5 = LDD Channel status
def test_GIVEN_ldd_control_is_ON_and_trigger_is_OFF_WHEN_lld_channel_command_is_set_ON_THEN_channel_status_is_NOT_ON():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] != '1'

    
# Sending command b"\x08\x00\x01\x00\x00\x00\x1"
# Sending command b"\x09\x00\x01\x00\x00\x00\x00"
# Sending command b"\x0A\x00\x01\x00\x00\x00\x00"
# Sending command b"\x0A\x00\x01\x00\x00\x00\x01"
# Sending command b"\x02\x00\x00\x00\x00\x00"
# Byte 6, Bit 5 = LDD Channel status
def test_GIVEN_ldd_control_is_ON_trigger_is_ON_channel_is_ON_WHEN_lld_trigger_command_is_set_OFF_THEN_channel_status_and_trigger_is_NOT_ON():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Control <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD trigger <<", receive(b"\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[6:7]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] != '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] != '1'


def test_GIVEN_ldd_trigger_is_OFF_and_lld_trigger_SOURCE_command_is_EXTERNAL_then_LDD_Frequency_is_NOT_SET():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Control <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    trig_mode = '0'
    trig_edge = '0'
    trig_source = '1'
    trigger_settings = int(trig_mode + trig_edge + trig_source,2).to_bytes(length = 1, byteorder = "little", signed = False)
    socket.send(b"\x0F\x00\x01\x00\x00\x00"+trigger_settings)
    print("\n trigger settings <<", receive(b"\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    set_value = 5.0
    socket.send(b"\x0D\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value))
    print("\n LDD Frequency set <<", receive(b"\x0D", b"\x0D\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value)))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n LDD Frequency <<",struct.unpack("<f", status_data[8:12])[0])
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '1'
    assert_that(struct.unpack("<f", status_data[8:12])[0], is_not(close_to(set_value,5.0)))
    
    
def test_GIVEN_ldd_trigger_is_OFF_and_lld_Frequency_is_SET_then_LDD_Frequency_is_NOT_SET():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Control <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    set_value = 5.0
    socket.send(b"\x0D\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value))
    print("\n LDD Frequency set <<", receive(b"\x0D", b"\x0D\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value)))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n LDD Frequency <<",struct.unpack("<f", status_data[8:12])[0])
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '1'
    assert_that(struct.unpack("<f", status_data[8:12])[0], is_not(close_to(set_value,5.0)))


def test_GIVEN_ldd_is_Connected_tigger_is_ON_and_channel_is_ON_and_ldd_softstart_command_is_ENABLED_WHEN_ldd_pulse_current_IS_SET_THEN_ldd_pulse_current_is_NOT_SET_WITHIN_TIME():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x15\x00\x01\x00\x00\x00\x01")
    print("\n LDD Soft Start <<", receive(b"\x15", b"\x15\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time*6)
    socket.send(b"\x0B\x00\x04\x00\x00\x00" + (0).to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse current set <<", receive(b"\x0B", b"\x0B\x00\x04\x00\x00\x00" + (0).to_bytes(length=4, byteorder="little", signed=False)))
    time.sleep(sleep_time*6)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[40:41]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '1'
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[7] == '1'
    set_value = 30
    socket.send(b"\x0B\x00\x04\x00\x00\x00" + set_value.to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse current set <<", receive(b"\x0B", b"\x0B\x00\x04\x00\x00\x00" + set_value.to_bytes(length=4, byteorder="little", signed=False)))
    time.sleep(sleep_time*6)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n Pulse Current <<",int.from_bytes(status_data[24:28], byteorder="little", signed=False))
    assert_that(int.from_bytes(status_data[24:28], byteorder="little", signed=False), is_not(close_to(set_value,5)))
    socket.send(b"\x15\x00\x01\x00\x00\x00\x01")
    print("\n LDD Soft Start <<", receive(b"\x15", b"\x15\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time*6)

def test_GIVEN_ldd_is_Connected_tigger_is_ON_and_channel_is_OFF_and_ldd_softstart_command_is_DISABLED_WHEN_ldd_pulse_current_IS_SET_THEN_ldd_pulse_current_is_NOT_SET():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x15\x00\x01\x00\x00\x00\x00")
    print("\n LDD Soft Start <<", receive(b"\x15", b"\x15\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time*6)
    socket.send(b"\x0B\x00\x04\x00\x00\x00" + (0).to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse current set <<", receive(b"\x0B", b"\x0B\x00\x04\x00\x00\x00" + (0).to_bytes(length=4, byteorder="little", signed=False)))
    time.sleep(sleep_time*6)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x15\x00\x01\x00\x00\x00\x00")
    print("\n LDD Soft Start <<", receive(b"\x15", b"\x15\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time*6)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n status <<",bin(ord(status_data[40:41]))[2:].rjust(8, '0'))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '1'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '1'
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[7] == '0'
    set_value = 20
    socket.send(b"\x0B\x00\x04\x00\x00\x00" + set_value.to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse current set <<", receive(b"\x0B", b"\x0B\x00\x04\x00\x00\x00" + set_value.to_bytes(length=4, byteorder="little", signed=False)))
    time.sleep(sleep_time*6)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n Pulse Current <<",int.from_bytes(status_data[24:28], byteorder="little", signed=False))
    assert_that(int.from_bytes(status_data[24:28], byteorder="little", signed=False), is_not(close_to(set_value,5)))
    socket.send(b"\x15\x00\x01\x00\x00\x00\x01")
    print("\n LDD Soft Start <<", receive(b"\x15", b"\x15\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time*6)

    
def test_GIVEN_ldd_prerequsites_are_OFF_and_soft_start_is_OFF_WHEN_lld_pulse_current_command_is_set_THEN_pulse_current_is_NOT_SET():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x15\x00\x01\x00\x00\x00\x00")
    print("\n LDD Soft Start <<", receive(b"\x15", b"\x15\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time*6)
    socket.send(b"\x0B\x00\x04\x00\x00\x00" + (0).to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse current set <<", receive(b"\x0B", b"\x0B\x00\x04\x00\x00\x00" + (0).to_bytes(length=4, byteorder="little", signed=False)))
    time.sleep(sleep_time*6)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n LDD Operational<<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    set_value = 10
    socket.send(b"\x0B\x00\x04\x00\x00\x00" + set_value.to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse current set <<", receive(b"\x0B", b"\x0B\x00\x04\x00\x00\x00" + set_value.to_bytes(length=4, byteorder="little", signed=False)))
    time.sleep(sleep_time*6)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n Pulse Current <<",int.from_bytes(status_data[24:28], byteorder="little", signed=False))
    assert_that(int.from_bytes(status_data[24:28], byteorder="little", signed=False), is_not(close_to(set_value,5)))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '0'
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[1] == '0'
    socket.send(b"\x15\x00\x01\x00\x00\x00\x01")
    print("\n LDD Soft Start <<", receive(b"\x15", b"\x15\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time*6)


def test_GIVEN_ldd_prerequsites_are_OFF_WHEN_lld_bias_current_command_is_set_THEN_bias_current_is_NOT():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)    
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n LDD Operational<<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    set_value = 2.0
    socket.send(b"\x0C\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value))
    print("\n bias current set <<", receive(b"\x0C", b"\x0C\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value)))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n Bias Current <<",struct.unpack("<f", status_data[32:36])[0])
    assert_that(struct.unpack("<f", status_data[32:36])[0], is_not(close_to(set_value,1.0)))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '0'
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[1] == '0'

def test_GIVEN_ldd_prerequsites_are_OFF_WHEN_lld_frequency_command_is_set_THEN_frequency_is_NOT():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n LDD Operational<<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    set_value = 10.0
    socket.send(b"\x0D\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value))
    print("\n LDD Frequency set <<", receive(b"\x0D", b"\x0D\x00\x04\x00\x00\x00" +  struct.pack("<f", set_value)))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("\n LDD Frequency <<",struct.unpack("<f", status_data[8:12])[0])
    assert_that(struct.unpack("<f", status_data[8:12])[0], is_not(close_to(set_value,5.0)))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '0'
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[1] == '0'

def test_GIVEN_ldd_prerequsites_are_OFF_WHEN_lld_pulse_width_command_is_set_THEN_pulse_width_is_NOT_set_close_to_setting():
    socket.send(b"\x08\x00\x01\x00\x00\x00\x01")
    print("\n LDD Operational <<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x01")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x01")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x01"))
    time.sleep(sleep_time)
    socket.send(b"\x0A\x00\x01\x00\x00\x00\x00")
    print("\n LDD Channel <<", receive(b"\x0A", b"\x0A\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x09\x00\x01\x00\x00\x00\x00")
    print("\n LDD Trigger <<", receive(b"\x09", b"\x09\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    socket.send(b"\x08\x00\x01\x00\x00\x00\x00")
    print("\n LDD Operational<<", receive(b"\x08", b"\x08\x00\x01\x00\x00\x00\x00"))
    time.sleep(sleep_time)
    set_value = 202
    socket.send(b"\x0E\x00\x04\x00\x00\x00" +  set_value.to_bytes(length=4, byteorder="little", signed=False))
    print("\n pulse width set <<", receive(b"\x0E", b"\x0E\x00\x04\x00\x00\x00" +  set_value.to_bytes(length=4, byteorder="little", signed=False)))
    time.sleep(sleep_time)
    socket.send(b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data >>", b"\x02\x00\x00\x00\x00\x00")
    status_data = receive(b"\x02", b"\x02\x00\x00\x00\x00\x00")
    print("\n driver data <<", status_data)
    print("status data ", status_data)
    print("pulse width data ", status_data[16:20])
    print("\n Pulse Width <<",int.from_bytes(status_data[16:20], byteorder="little", signed=False))
    assert_that(int.from_bytes(status_data[16:20], byteorder="little", signed=False), is_not(close_to(set_value,5)))
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[5] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[6] == '0'
    assert bin(ord(status_data[6:7]))[2:].rjust(8, '0')[7] == '0'
    assert bin(ord(status_data[40:41]))[2:].rjust(8, '0')[1] == '0'
