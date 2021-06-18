#!/usr/bin/env python3
import struct
import bitarray

get_sta_output = b'\x18'
print(bin(ord(get_sta_output))[2:].rjust(8, "0"))






#ldd_triggers = "{8:b}".format(int((get_pm_sta_output).hex(), 8))

#print(ldd_triggers)
# byte = '01'
# byte = byte.ljust(8, '0')
# print(byte)


# status = bin(get_sta_output[0])[2:]
# for x in range (8-len(status)): #filling upto 8 bits
#     status = status + "0"
# print("status", status)

# pm_temperature_bytes = get_pm_sta_output[0:4]
# print(pm_temperature_bytes)
# pm_temperature_float = struct.unpack("<f", pm_temperature_bytes)[0]
# print("Pulse Module Temperature is : %f" % pm_temperature_float)

# pm_humidity_bytes = get_pm_sta_output[4:8]
# print(pm_humidity_bytes)
# pm_humidity_float = struct.unpack("<f", pm_humidity_bytes)[0]
# print("Pulse Module Humidity is : %f" % pm_humidity_float)

# pm_water_flow_bytes = get_pm_sta_output[8:12]
# print(pm_water_flow_bytes)
# pm_water_flow_float = struct.unpack("<f", pm_water_flow_bytes)[0]
# print("Pulse Module Water Flow is : %f" % pm_water_flow_float)

# pm_error_status = bin(get_pm_sta_output[12])[2:].zfill(6)
# print(pm_error_status)
# tcp_connection_error = pm_error_status[0]
# if tcp_connection_error == "0":
#     print("no error in TCP",tcp_connection_error)
# elif tcp_connection_error == "1":
#     print("TCP Connection Error",tcp_connection_error)
# leakage_error = pm_error_status[1]
# if leakage_error == "0":
#     print("no error in leakage",leakage_error)
# elif leakage_error == "1":
#     print("Leakage Error",leakage_error)
# forward_voltage_error = pm_error_status[2]
# if forward_voltage_error == "0":
#     print("no error in forward voltage",forward_voltage_error)
# elif forward_volta:ge_error == "1":
#     print("Forward Voltage Error",forward_voltage_error)
# temperature_error = pm_error_status[3]
# if temperature_error == "0":
#     print("no error in temperature",temperature_error)
# elif temperature_error == "1":
#     print("Temperature Error",temperature_error)
# humidity_error = pm_error_status[4]
# if humidity_error == "0":
#     print("no error in humidity",humidity_error)
# elif humidity_error == "1":
#     print("Humidity Error",humidity_error)
# water_flow_error = pm_error_status[5]
# if water_flow_error == "0":
#     print("no error in water flow",water_flow_error)
# elif water_flow_error == "1":
#     print("Water Flow error",water_flow_error)

# pulse_counter_bytes = get_pm_sta_output[13:]
# print("pulse_counter_bytes",pulse_counter_bytes)
# pulse_counter_float = struct.unpack("<f", pulse_counter_bytes)[0]
# print("Pulse Module pulse counter is : %f" % pulse_counter_float)