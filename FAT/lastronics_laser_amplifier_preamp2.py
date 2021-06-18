#!/usr/bin/env python3
import socket
from macros import *
import time
import struct
import config

class LastronicsLaserAmplifierPreAmp2:
    def __init__(self, device_ip, device_port):
        self._command_dict = self._init_command_dict()
        self.device_ip = device_ip
        self.device_port = device_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.open_connection()
        self.get_ldd_sta()
        self.trig_edge = self.trigger_edge
        self.trig_source = self.trigger_source
        self.trig_mode = self.trigger_mode


    def _init_command_dict(self):
        return {
            #understanding_commands: b- indicates bytes"'command lsb''command msb''length low byte''length high byte''length higher byte''data''data''data''data''data'....." 
            "set_connect_ldd": b"\x17\x00\x00\x00\x00\x00\x00",
            "set_connect_pm": b"\x19\x00\x00\x00\x00\x00\x00",
            "set_connect_amplifier": b"\x22\x00\x00\x00\x00\x00\x00",
            "set_connect_chiller": b"\x16\x00\x00\x00\x00\x00\x00",
            "set_connect_itlk": b"\x18\x00\x00\x00\x00\x00\x00",
            "set_ldd_ctrl": b"\x08\x00\x01\x00\x00\x00",
            "set_ldd_trig": b"\x09\x00\x01\x00\x00\x00",
            "set_ldd_chan": b"\x0A\x00\x01\x00\x00\x00",
            "set_ldd_pcur": b"\x0B\x00\x04\x00\x00\x00",
            "set_ldd_bcur": b"\x0C\x00\x04\x00\x00\x00",
            "set_ldd_freq": b"\x0D\x00\x04\x00\x00\x00",
            "set_ldd_pwid": b"\x0E\x00\x04\x00\x00\x00",
            "set_ldd_trig_settings": b"\x0F\x00\x01\x00\x00\x00",  # trigger settings on and off only
            "set_ldd_softstart": b"\x15\x00\x01\x00\x00\x00", # soft start 
            "get_ldd_err": b"\x13\x00\x00\x00\x00\x00",  # driver error ack
            "get_ldd_sta": b"\x02\x00\x00\x00\x00\x00",
            "get_pm_sta": b"\x03\x00\x00\x00\x00\x00",
            "get_amp_sta": b"\x04\x00\x00\x00\x00\x00",
            "get_water_chil_sta": b"\x05\x00\x00\x00\x00\x00",
            "get_interlock_sta": b"\x07\x00\x00\x00\x00\x00",
            "set_chil_ctrl": b"\x10\x00\x01\x00\x00\x00",
            "set_water_chil_temp": b"\x11\x00\x04\x00\x00\x00",
            "set_amp_ctrl": b"\x12\x00\x01\x00\x00\x00",
            "get_chil_err": b"\x14\x00\x00\x00\x00\x00",
            "set_amp_temp": b"\x23\x00\x04\x00\x00\x00",
            "set_interlock_rst": b"\x24\x00\x00\x00\x00\x00",
            ############ Diagnoistics Commands #############
            "set_spa_divider": b"\x04\x11\x04\x00\x00\x00",
            "set_spa_gain": b"\x05\x00\x11\x04\x00\x00\x00",
            "set_spa_black_lvl_gain": b"\x06\x11\x04\x00\x00\x00",
            "set_spa_trig_mode": b"\x07\x11\x04\x00\x00\x00",
            "set_spa_trig_src": b"\x08\x11\x04\x00\x00\x00",
            "set_spa_trig_edge": b"\x09\x11\x04\x00\x00\x00",
            "set_spa_trig_delay": b"\x0A\x11\x08\x00\x00\x00",
            "set_spa_expos_time": b"\x0B\x11\x08\x00\x00\x00",
            "set_spa_save_backgnd": b"\x0D\x11\x01\x00\x00\x00",
            "set_spa_sub_backgnd": b"\x0E\x11\x01\x00\x00\x00",
            "set_spa_n_backgnd_avgs": b"\x0F\x11\x04\x00\x00\x00",
            "get_spa_n_backgnd_avgs_done": b"\x10\x11\x00\x00\x00\x00",
            "set_spa_adjustments_mode": b"\x12\x11\x01\x00\x00\x00",
            "set_spa_images_avg": b"\x13\x11\x01\x00\x00\x00",
            "get_spa_n_pictures_in_stack": b"\x13\x11\x00\x00\x00\x00",
            "set_spa_cam_standard_properties": b"\x16\x11\x01\x00\x00\x00",
            "get_spa_far_field_xy_centroid": b"\x17\x11\x00\x00\x00\x00",
            "get_spa_near_field_xy_centroid": b"\x18\x11\x00\x00\x00\x00",
            "get_spa_far_field_delta_xy_centroid": b"\x19\x11\x00\x00\x00\x00",
            "get_spa_near_field_delta_xy_centroid": b"\x1A\x11\x00\x00\x00\x00",
            "get_spa_energy": b"\x1B\x11\x00\x00\x00\x00",
            "set_spa_energy_calib_factor": b"\x1C\x11\x04\x00\x00\x00",
            "set_spa_roi_near_field": b"\x1D\x11\x0C\x00\x00\x00",
            "set_spa_roi_far_field": b"\x1E\x11\x0C\x00\x00\x00",
            "set_spa_far_field_reff": b"\x1F\x11\x08\x00\x00\x00",
            "set_spa_near_field_reff": b"\x20\x11\x08\x00\x00\x00",
            "set_spa_gauss_order": b"\x21\x11\x04\x00\x00\x00",
            "set_spa_HWB": b"\x22\x11\x04\x00\x00\x00",
            "get_image":b"\x0C\x11\x00\x00\x00\x00",
            "get_histogram":b"\x15\x11\x00\x00\x00\x00",
        }

    def open_connection(self):
        self.socket.connect((self.device_ip, self.device_port))
    def close_connection(self):
        self.socket.close()

    def set_connect_ldd(self):
        self.ldd_ctrl = self.set_connection("set_connect_ldd")
        wait_time = config.short_wait
        print("Set Connect LDD")
        time.sleep(wait_time)
        self.get_connect_ldd()

    def set_connect_pump_module(self):
        self.ldd_ctrl = self.set_connection("set_connect_pm")
        wait_time = config.short_wait
        print("Set Connect Pump Module")
        time.sleep(wait_time)

    def set_connect_amplifier(self):
        self.ldd_ctrl = self.set_connection("set_connect_amplifier")
        wait_time = config.short_wait
        print("Set Connect Amplifier")
        time.sleep(wait_time)

    def set_connect_chiller(self):
        self.ldd_ctrl = self.set_connection("set_connect_chiller")
        wait_time = config.short_wait
        print("Set Connect Chiller")
        time.sleep(wait_time)

    def set_connect_interlock(self):
        self.ldd_ctrl = self.set_connection("set_connect_itlk")
        wait_time = config.short_wait
        print("Set Connect Interlock")
        time.sleep(wait_time)


    def set_ldd_ctrl(self, set_value):
        self.ldd_ctrl = self.set_parm("set_ldd_ctrl", set_value)
        wait_time = config.wait_to_set_laser_diode_driver_control_to_operational_or_standby
        print("wait time to set ldd control is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_ldd_ctrl()


    def set_ldd_trig(self, set_value):
        self.ldd_trig = self.set_parm("set_ldd_trig", set_value)
        wait_time = config.wait_to_set_laser_diode_driver_trigger_on_off
        print("wait time to set ldd trigger is ",wait_time, "Seconds")        
        time.sleep(wait_time)
        self.get_ldd_trig()


    def set_ldd_chan(self, set_value):  # set laser driver diode channel
        self.ldd_chan = self.set_parm("set_ldd_chan", set_value)
        wait_time = config.wait_to_set_laser_diode_driver_channel_status_on_off
        print("wait time to set ldd channel is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_ldd_chan() 


    def set_ldd_pulse_current(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
            length=4, byteorder="little", signed=False
        )
        if self.channel_status == TurnedOn:
           self.ldd_pcur_at_instance = self.set_parm("set_ldd_pcur",self.set_value_bytes)
        wait_time = config.medium_wait
        print("wait time to set Pulse Current is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_ldd_pcur()


    def set_ldd_pulse_width(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
            length=4, byteorder="little", signed=False
        )
        if self.channel_status == TurnedOn:
            self.ldd_pwid_at_instance = self.set_parm("set_ldd_pwid",self.set_value_bytes)
        wait_time = config.medium_wait
        print("wait time to set Pulse Width is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_ldd_pwid()

    def set_ldd_bias_current(self, set_value):
        self.set_value_bytes = struct.pack("<f", set_value)
        if self.channel_status == TurnedOn:
            self.ldd_bcur_at_instance = self.set_parm("set_ldd_bcur",self.set_value_bytes)
        wait_time = config.medium_wait
        print("wait time to set ldd Bias Current is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_ldd_bcur()

    def set_ldd_freq(self, set_value):
        self.set_value_bytes = struct.pack("<f", set_value)
        if self.trig_source == Internal:
            self.ldd_freq_at_instance = self.set_parm("set_ldd_freq",self.set_value_bytes)
        wait_time = config.medium_wait
        print("wait time to set ldd Frequency is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_ldd_freq()

    def set_ldd_trigger_settings(self, trig_mode, trig_edge, trig_source):
        set_value = trig_mode + trig_edge + trig_source
        set_value_bits =int(set_value,2)
        set_value_bytes = set_value_bits.to_bytes(
        length=1, byteorder="little", signed=False
        )
        self.ldd_tmod = self.set_parm("set_ldd_trig_settings", set_value_bytes)
        wait_time = config.wait_time_to_set_trigger_setting
        print("wait time to set ldd Trigger Setting is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_ldd_trigger_settings()
        
    def set_ldd_trigger_Continuous_single(self, set_value):
        self.get_ldd_trigger_settings()
        print("setting trig mode",set_value)
        self.set_ldd_trigger_settings(set_value,self.trigger_edge,self.trigger_source)

    def set_ldd_trigger_positive_negative(self, set_value):
        self.get_ldd_trigger_settings()
        print("setting trig edge",set_value)
        self.set_ldd_trigger_settings(self.trigger_mode,set_value,self.trigger_source)

    def set_ldd_trigger_internal_external(self, set_value):
        self.get_ldd_trigger_settings()
        print("setting trig source",set_value)
        self.set_ldd_trigger_settings(self.trigger_mode,self.trigger_edge,set_value)


    def set_water_chiller_control(self, set_value):
        self.chil_ctrl = self.set_parm("set_chil_ctrl", set_value)
        print("Setting Water Chiller Control")
        wait_time = config.short_wait
        time.sleep(wait_time)
        print("wait time to set Water Chiller control is ",wait_time," Seconds")
        self.get_chil_ctrl()

    def set_water_chiller_temperature_setpoint(self, set_value):
        self.set_value_bytes = struct.pack("<f", set_value)
        self.water_chil_temp = self.set_parm("set_water_chil_temp",self.set_value_bytes)
        wait_time = config.long_wait*2
        print("SET CHILLER TEMPERATURE Waiting time: ",wait_time," Seconds")
        time.sleep(wait_time)
        self.get_water_chil_setpoint_temperature()


    def set_amplifier_control(self, set_value):
        self.amplifier_ctrl = self.set_parm("set_amp_ctrl", set_value)
        wait_time = config.short_wait
        print("Setting Amplifier Control",wait_time," Seconds")
        time.sleep(wait_time)
        self.get_amplifier_ctrl()

    def set_amplifier_target_temperature(self, set_value):
        self.set_value_bytes = struct.pack("<f", set_value)
        #reading the acknowledgement from the device into amplifier_target_temperature
        self.amplifier_target_temp_bytes = self.set_parm("set_amp_temp", self.set_value_bytes)
        #waiting for a small time less than short_Wait
        wait_time = config.short_wait/2
        print("wait time to set Amplifier Target Temperature is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_amplifier_target_temperature(self.amplifier_target_temp_bytes[-4:])
    def get_amplifier_target_temperature(self,get_value_bytes):
        self.amplifier_target_temp_float = struct.unpack("<f", get_value_bytes)[0]
        return self.amplifier_target_temp_float

    def set_interlock_reset(self):
        #reading the acknowledgement from the device into interlock_reset
        self.interlock_reset = self.set_parm("set_interlock_rst", OFF)
        #waiting for a small time less than short_Wait
        wait_time = config.short_wait
        print("wait time to set Interlock Reset is ",wait_time, "Seconds")
        time.sleep(wait_time)


    def set_ldd_softstart(self, set_value):
        self.ldd_ctrl = self.set_parm("set_ldd_softstart", set_value)
        wait_time = config.short_wait
        print("wait time to set ldd SoftStart is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_ldd_softstart()


    def set_spatial_divider(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.spa_divider_bytes = self.set_parm("set_spa_divider", set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Divider is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spatial_divider(self.spa_divider_bytes[-4:]) 
    def get_spatial_divider(self, get_value_bytes):
        self.spa_divider = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_divider

    def set_spatial_gain(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.spa_gain_bytes = self.set_parm("set_spa_gain", set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Gain is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spatial_gain(self.spa_gain_bytes[-4:])
    def get_spatial_gain(self, get_value_bytes):
        self.spa_gain = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_gain

    def set_spatial_black_level_gain(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.spa_black_level_gain_bytes = self.set_parm("set_spa_black_lvl_gain", set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Black Level Gain is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spatial_black_level_gain(self.spa_black_level_gain_bytes[-4:])
    def get_spatial_black_level_gain(self, get_value_bytes):
        self.spa_black_level_gain = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_black_level_gain

    def set_spatial_trigger_mode(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.spa_trigger_mode_bytes = self.set_parm("set_spa_trig_mode", set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Trigger Mode is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spatial_trigger_mode(self.spa_trigger_mode_bytes[-4:])
    def get_spatial_trigger_mode(self, get_value_bytes):
        self.spa_trigger_mode = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_trigger_mode

    def set_spatial_trigger_source(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.spa_trigger_source_bytes = self.set_parm("set_spa_trig_src", set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Trigger Source is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spatial_trigger_source(self.spa_trigger_source_bytes[-4:])
    def get_spatial_trigger_source(self, get_value_bytes):
        self.spa_trigger_source = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_trigger_source

    def set_spatial_trigger_edge(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.spa_trigger_edge_bytes = self.set_parm("set_spa_trig_edge", set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Trigger Edge is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spatial_trigger_edge(self.spa_trigger_edge_bytes[-4:])
    def get_spatial_trigger_edge(self, get_value_bytes):
        self.spa_trigger_edge = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_trigger_edge

    def set_spatial_trigger_delay_absloute(self, set_value):
        if (set_value <= 0.0 and set_value <= 1000.0):
            self.set_value_bytes = struct.pack("<d", set_value) #specifying double since 8 bytes needed to be sent
            self.spa_trigger_delay_absloute_bytes = self.set_parm("set_spa_trig_delay", set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Trigger Delay Absolute is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spatial_trigger_delay_absloute(self.spa_trigger_delay_absloute_bytes[-8:])
    def get_spatial_trigger_delay_absloute(self, get_value_bytes):
        self.spa_trigger_delay_absloute = struct.unpack("<d", get_value_bytes)
        return self.spa_trigger_delay_absloute

    def set_spatial_exposure_time_absloute(self, set_value):
        if (set_value <= 0.02 and set_value <= 10000.0):             
            self.set_value_bytes = struct.pack("<d", set_value) #specifying double since 8 bytes needed to be sent
            self.spa_exposure_time_absloute_bytes = self.set_parm("set_spa_expos_time", set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Exposure Time Absolute is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spatial_exposure_time_absloute(self.spa_exposure_time_absloute_bytes[-8:])
    def get_spatial_exposure_time_absloute(self, get_value_bytes):
        self.spa_exposure_time_absloute = struct.unpack("<d", get_value_bytes)
        return self.spa_exposure_time_absloute

    def set_spa_save_background(self, set_value):
        self.spa_save_background = self.set_parm("set_spa_save_backgnd", set_value)
        wait_time = config.short_wait
        print("wait time to set Spatial Save Background is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.spa_save_background_return_val = self.spa_save_background[-1:] # store the last byte of ack from the device

    def set_spa_substract_background(self, set_value):
        self.spa_sub_background = self.set_parm("set_spa_sub_backgnd", set_value)
        wait_time = config.short_wait
        print("wait time to set Spatial Substract Background is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.spa_substract_background_return_val = self.spa_sub_background[-1:] # store the last byte of ack (\x00 or \x01) from the device

    def set_spa_N_background_averages(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.set_parm("set_spa_n_backgnd_avgs", self.set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Background Averages is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spa_N_background_averages()
    def get_spa_N_background_averages(self):
        self.spa_n_backgnd_avgs = self.get_parm("get_spa_n_backgnd_avgs_done")
        self.spa_n_backgnd_avgs_return_val_bytes = self.spa_n_backgnd_avgs[-4:]
        self.spa_n_backgnd_avgs_return_val = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_n_backgnd_avgs_return_val

    def set_spa_number_of_ticks_in_ledgend(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.spa_number_of_ticks_in_ledgend_bytes = self.set_parm("set_spa_n_backgnd_avgs", self.set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Number of Ticks in Ledgend is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spa_number_of_ticks_in_ledgend(self.spa_number_of_ticks_in_ledgend_bytes[-4:])
    def get_spa_number_of_ticks_in_ledgend(self,get_value_bytes):
        self.spa_number_of_ticks_in_ledgend_return_val = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_number_of_ticks_in_ledgend_return_val

    def set_spa_adjustments_mode(self, set_value):
        self.spa_adjustments_mode = self.set_parm("set_spa_adjustments_mode", self.set_value)
        wait_time = config.short_wait
        print("wait time to set Spatial Adjustments Mode is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.spa_adjustments_mode_return_val = self.spa_adjustments_mode[-1:]

    def set_spa_image_averages(self, set_value):
        self.set_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.spa_image_average_bytes = self.set_parm("set_images_avg", self.set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Images Averages is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spa_image_averages(self.spa_image_average_bytes[-4:])
    def get_spa_image_averages(self,get_value_bytes):
        self.spa_image_average_return_val = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_image_average_return_val

    def get_spa_N_pictures_in_stack(self):
        self.spa_N_pictures_in_stack = self.get_parm("get_spa_n_backgnd_avgs_done")
        self.spa_N_pictures_in_stack_return_val_bytes = self.spa_N_pictures_in_stack[-4:]
        self.spa_N_pictures_in_stack_return_val = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_n_backgnd_avgs_return_val

    def set_spa_camera_standard_properties(self, set_value):
        self.spa_cam_standard_properties = self.set_parm("set_spa_cam_standard_properties", set_value)
        wait_time = config.short_wait
        print("wait time to set Spatial Camera Standard Properties is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.spa_cam_standard_properties_return_val = self.spa_cam_standard_properties[-1:] # store the last byte of ack from the device

    def get_spa_far_field_XY_centroid(self):
        self.spa_far_field_XY_centroid = self.get_parm("get_spa_far_field_xy_centroid")
        self.spa_far_field_XY_centroid_return_value = struct.unpack("<d", self.spa_far_field_XY_centroid)
        self.spa_far_field_X_centroid_return_value = self.spa_far_field_XY_centroid_return_value[0:4]
        self.spa_far_field_Y_centroid_return_value = self.spa_far_field_XY_centroid_return_value[4:]
        return self.spa_far_field_X_centroid_return_value,self.spa_far_field_Y_centroid_return_value

    def get_spa_near_field_XY_centroid(self):
        self.spa_near_field_XY_centroid = self.get_parm("get_spa_near_field_xy_centroid")
        self.spa_near_field_XY_centroid_return_value = struct.unpack("<d", self.spa_near_field_XY_centroid)
        self.spa_near_field_X_centroid_return_value = self.spa_near_field_XY_centroid_return_value[0:4]
        self.spa_near_field_Y_centroid_return_value = self.spa_near_field_XY_centroid_return_value[4:]
        return self.spa_near_field_X_centroid_return_value,self.spa_near_field_Y_centroid_return_value

    def get_spa_far_field_delta_XY_centroid(self):
        self.spa_far_field_delta_XY_centroid = self.get_parm("get_spa_far_field_delta_xy_centroid")
        self.spa_far_field_delta_XY_centroid_return_value = struct.unpack("<d", self.spa_far_field_delta_XY_centroid)
        self.spa_far_field_delta_X_centroid_return_value = self.spa_far_field_delta_XY_centroid_return_value[0:4]
        self.spa_far_field_delta_Y_centroid_return_value = self.spa_far_field_delta_XY_centroid_return_value[4:]
        return self.spa_far_field_delta_X_centroid_return_value,self.spa_far_field_delta_Y_centroid_return_value

    def get_spa_near_field_delta_XY_centroid(self):
        self.spa_near_field_delta_XY_centroid = self.get_parm("get_spa_near_field_delta_xy_centroid")
        self.spa_near_field_delta_XY_centroid_return_value = struct.unpack("<d", self.spa_near_field_delta_XY_centroid)
        self.spa_near_field_delta_X_centroid_return_value = self.spa_near_field_delta_XY_centroid_return_value[0:4]
        self.spa_near_field_delta_Y_centroid_return_value = self.spa_near_field_delta_XY_centroid_return_value[4:]
        return self.spa_near_field_delta_X_centroid_return_value,self.spa_near_field_delta_Y_centroid_return_value

    def get_spa_energy(self):
        self.spa_energy = self.get_parm("get_spa_energy")
        self.spa_energy_return_value = struct.unpack("<f", self.spa_energy)
        return self.spa_energy_return_value

    def set_spa_energy_calibration_factor(self, set_value):
        self.set_value_bytes = struct.pack("<f", set_value)
        self.spa_energy_calibration_factor = self.set_parm("set_spa_energy_calib_factor", self.set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Energy Calibration Factor is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spa_energy_calibration_factor(self.spa_energy_calibration_factor[-4:])
    def get_spa_energy_calibration_factor(self,get_value_bytes):
        self.spa_energy_calibration_factor_return_val = struct.unpack("<d", get_value_bytes)
        return self.spa_energy_calibration_factor_return_val

    def set_spa_ROI_near_field(self, set_x_value, set_y_value, set_rad_value):
        self.set_x_value_bytes = set_x_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.set_y_value_bytes = set_y_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.set_radian_value_bytes = set_rad_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.set_value_bytes = self.set_x_value_bytes + self.set_y_value_bytes + self.set_radian_value_bytes
        self.set_value_bytes = set_value.to_bytes(
        length=12, byteorder="little", signed=False
        )
        self.spa_ROI_near_field_bytes = self.set_parm("set_spa_roi_near_field", self.set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial ROI near Field is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spa_ROI_near_field(self.spa_ROI_near_field_bytes[-12:])
    def get_spa_ROI_near_field(self,get_value_bytes):
        get_x_value_bytes = get_value_bytes[0:4]
        get_y_value_bytes = get_value_bytes[4:8]
        get_rad_value_bytes = get_value_bytes[8:]
        self.spa_ROI_near_field_x_return_val = int.from_bytes(
            get_x_value_bytes, byteorder="little", signed=False
        )
        self.spa_ROI_near_field_y_return_val = int.from_bytes(
            get_y_value_bytes, byteorder="little", signed=False
        )
        self.spa_ROI_near_field_rad_return_val = int.from_bytes(
            get_rad_value_bytes, byteorder="little", signed=False
        )
        return self.spa_ROI_near_field_x_return_val,self.spa_ROI_near_field_y_return_val,self.spa_ROI_near_field_rad_return_val

    def set_spa_ROI_far_field(self, set_x_value, set_y_value, set_rad_value):
        self.set_x_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.set_y_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.set_radian_value_bytes = set_value.to_bytes(
        length=4, byteorder="little", signed=False
        )
        self.set_value_bytes = self.set_x_value_bytes + self.set_y_value_bytes + self.set_radian_value_bytes
        self.spa_ROI_far_field_bytes = self.set_parm("set_spa_roi_far_field", self.set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial ROI far Field is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spa_ROI_far_field(self.spa_ROI_far_field_bytes[-12:])
    def get_spa_ROI_far_field(self,get_value_bytes):
        get_x_value_bytes = get_value_bytes[0:4]
        get_y_value_bytes = get_value_bytes[4:8]
        get_rad_value_bytes = get_value_bytes[8:]
        self.spa_ROI_far_field_x_return_val = int.from_bytes(
            get_x_value_bytes, byteorder="little", signed=False
        )
        self.spa_ROI_far_field_y_return_val = int.from_bytes(
            get_y_value_bytes, byteorder="little", signed=False
        )
        self.spa_ROI_far_field_rad_return_val = int.from_bytes(
            get_rad_value_bytes, byteorder="little", signed=False
        )
        return self.spa_ROI_far_field_x_return_val, self.spa_ROI_far_field_y_return_val, self.spa_ROI_far_field__return_val

    def set_spa_far_field_reference(self, set_x_value, set_y_value):
        self.set_x_value_bytes = struct.pack("<f", set_x_value)
        self.set_y_value_bytes = struct.pack("<f", set_y_value)
        self.set_value_bytes = self.set_x_value_bytes + self.set_y_value_bytes 
        self.spa_far_field_reference_bytes = self.set_parm("set_spa_far_field_reff", self.set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial ROI far Field Reference is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spa_far_field_reference(self.spa_far_field_reference_bytes[-8:])
    def get_spa_far_field_reference(self,get_value_bytes):
        get_x_value_bytes = get_value_bytes[0:4]
        get_y_value_bytes = get_value_bytes[4:]
        self.spa_far_field_reference_x_return_val =struct.unpack("<f",get_x_value_bytes)
        self.spa_far_field_reference_y_return_val =struct.unpack("<f",get_y_value_bytes)
        return self.spa_far_field_reference_x_return_val,self.spa_far_field_reference_y_return_val

    def set_spa_near_field_reference(self, set_x_value, set_y_value):
        self.set_x_value_bytes = struct.pack("<f", set_x_value)
        self.set_y_value_bytes = struct.pack("<f", set_y_value)
        self.set_value_bytes = self.set_x_value_bytes + self.set_y_value_bytes  
        self.spa_near_field_reference_bytes = self.set_parm("set_spa_near_field_reff", self.set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial ROI near Field Reference is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spa_near_field_reference(self.spa_near_field_reference_bytes[-8:])
    def get_spa_near_field_reference(self,get_value_bytes):
        get_x_value_bytes = get_value_bytes[0:4]
        get_y_value_bytes = get_value_bytes[4:]
        self.spa_near_field_reference_x_return_val =struct.unpack("<f",get_x_value_bytes)
        self.spa_near_field_reference_y_return_val =struct.unpack("<f",get_y_value_bytes)
        return self.spa_near_field_reference_x_return_val,self.spa_near_field_reference_y_return_val

    def set_spa_gauss_order(self, set_value):
        self.set_value_bytes = struct.pack("<d", set_value)
        self.spa_gauss_order_bytes = self.set_parm("set_spa_gauss_order", self.set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial Gauss Order is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spa_gauss_order(self.spa_near_field_reference_bytes[-8:])
    def get_spa_gauss_order(self,get_value_bytes):
        self.spa_gauss_order_return_val = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_gauss_order_return_val
        
    def set_spa_HWB(self, set_value):
        self.set_value_bytes = struct.pack("<d", set_value)
        self.spa_HWB_bytes = self.set_parm("set_spa_HWB", self.set_value_bytes)
        wait_time = config.short_wait
        print("wait time to set Spatial HWB is ",wait_time, "Seconds")
        time.sleep(wait_time)
        self.get_spa_HWB(self.spa_HWB_bytes[-8:])
    def get_spa_HWB(self,get_value_bytes):
        self.spa_HWB_return_val = int.from_bytes(
            get_value_bytes, byteorder="little", signed=False
        )
        return self.spa_HWB_return_val


###############################################################################################
    def get_chil_err(self):
        self.chil_err = self.get_parm("get_chil_err")
        # returns 2 bytes of data that is to be converted into integer and each integer corresponds to specific error
        self.chil_err_output = self.chil_err[-2:]
        self.water_chil_error_status1 = int.from_bytes(self.chil_err_output[0:1] , byteorder='little')
        self.water_chil_error_status_int = bin(self.water_chil_error_status1)[2:].rjust(8, '0')
        self.low_temp_error = self.water_chil_error_status_int[0]
        self.high_temp_error = self.water_chil_error_status_int[1]
        self.low_temp_warning = self.water_chil_error_status_int[2]
        self.high_temp_warning = self.water_chil_error_status_int[3]
        self.water_chil_water_flow_error = self.water_chil_error_status_int[4]
        self.low_pressure_error = self.water_chil_error_status_int[5]
        self.water_chil_water_level_error = self.water_chil_error_status_int[6]
        self.water_chil_dry_run_error = self.water_chil_error_status_int[7]
        # water chiller error status2 compromises data of 2 parameters pressure and remote, in 2 bits, converting 
        #rjust is filling upto 2 bits
        self.water_chil_error_status2 = bin(ord(self.chil_err_output[1:2]))[2:].rjust(8,'0')
        self.high_pressure_error = self.water_chil_error_status2[6]
        self.remote_control_error = self.water_chil_error_status2[7]
    def get_low_temp_error(self):
        self.get_chil_err()
        return self.low_temp_error
    def get_high_temp_error(self):
        self.get_chil_err()
        return self.high_temp_error
    def get_low_temp_warning(self):
        self.get_chil_err()
        return self.low_temp_warning
    def get_high_temp_warning(self):
        self.get_chil_err()
        return self.high_temp_warning
    def get_water_chil_water_flow_error(self):
        self.get_chil_err()
        return self.water_chil_water_flow_error
    def get_low_pressure_error(self):
        self.get_chil_err()
        return self.low_pressure_error
    def get_water_chil_water_level_error(self):
        self.get_chil_err()
        return self.water_chil_water_level_error
    def get_water_chil_dry_run_error(self):
        self.get_chil_err()
        return self.water_chil_dry_run_error
    def get_high_pressure_error(self):
        self.get_chil_err()
        return self.low_temp_error
    def get_remote_control_error(self):
        self.get_chil_err()
        return self.remote_control_error





    def get_ldd_err(self):
        self.ldd_err = self.get_parm("get_ldd_err")
        # returns 1 bytes of data that is to be converted into integer and each integer corresponds to specific error
        self.ldd_err = int.from_bytes(self.ldd_err[-1:] , byteorder='little')
    def get_internal_bus_err(self):
        self.get_ldd_err()
        if self.ldd_err == 1:
            self.internal_bus_err = 1
        else: 
            self.internal_bus_err = 0
        return self.internal_bus_err
    def get_mosfet_temp_err(self):
        self.get_ldd_err()
        if self.ldd_err == 2:
            self.mosfet_temp_err = 1
        else: 
            self.mosfet_temp_err = 0
        return self.mosfet_temp_err
    def get_capacitor_temp_err(self):
        self.get_ldd_err()
        if self.ldd_err == 3:
            self.capacitor_temp_err = 1
        else: 
            self.capacitor_temp_err = 0
        return self.capacitor_temp_err
    def get_heatsink_temp_err(self):
        self.get_ldd_err()
        if self.ldd_err == 3:
            self.heatsink_temp_err = 1
        else: 
            self.heatsink_temp_err = 0
        return self.heatsink_temp_err
    def get_interlock_err(self):
        self.get_ldd_err()
        if self.ldd_err == 8:
            self.interlock_err = 1
        else: 
            self.interlock_err = 0
        return self.interlock_err
    def get_pulse_shape_err(self):
        self.get_ldd_err()
        if self.ldd_err == 9:
            self.pulse_shape_err = 1
        else: 
            self.pulse_shape_err = 0
        return self.pulse_shape_err
    def get_smps_power_err(self):
        self.get_ldd_err()
        if self.ldd_err == 12:
            self.smps_power_err = 1
        else: 
            self.smps_power_err = 0
        return self.smps_power_err
    def get_smps_temp_err(self):
        self.get_ldd_err()
        if self.ldd_err == 15:
            self.smps_temp_err = 1
        else: 
            self.smps_temp_err = 0
        return self.smps_temp_err
    def get_capacitor_charge_err(self):
        self.get_ldd_err()
        if self.ldd_err == 17:
            self.capacitor_charge_err = 1
        else: 
            self.capacitor_charge_err = 0
        return self.capacitor_charge_err

    def set_big_endian(self, input_byte):
        #rjust is filling upto 8 bits
        return bin(ord(input_byte))[2:].rjust(8, '0')

    def get_ldd_sta(self):
        self.ldd_sta = self.get_parm("get_ldd_sta")
        # 35 = get the last 35 bytes from the 41 bytes 
        self.get_sta_output = self.ldd_sta[-35:]
        # 0:1 gets the first byte, is status for all ldd control parameters
        # 2: is for discarding the '0b' which bin function generates (eg  8 - 0b100 = 100)
        print("status = ",self.get_sta_output[0:1])
        self.status = self.set_big_endian(self.get_sta_output[0:1])
        self.trigger_mode = self.status[0]
        self.trigger_edge = self.status[1]
        self.trigger_source = self.status[2]
        self.capacitor_status = self.status[3]
        self.connection_status = self.status[4]
        self.channel_status = self.status[5]
        self.trigger_status = self.status[6]
        self.ldd_ctrl_mode = self.status[7]
        # frequency data is 4 bytes of data from byte 2 to 5th byte both inclusive 
        self.frequency_bytes = self.get_sta_output[2:6]
        # max frequency data is 4 bytes of data from byte 6 to 9th byte both inclusive 
        self.max_freq_bytes = self.get_sta_output[6:10]
        self.max_frequency_float = struct.unpack("<f", self.max_freq_bytes)[0]
        #pulse width data is 4 bytes of data from byte 10 to 13th byte both inclusive 
        self.pulse_width_bytes = self.get_sta_output[10:14]
        # max pulse width data is 4 bytes of data from byte 14 to 17th byte both inclusive 
        self.max_pulse_width_bytes = self.get_sta_output[14:18]
        self.max_pulse_width_int = int.from_bytes(
            self.max_pulse_width_bytes, byteorder="little", signed=False
        )
        # pulse current data is 4 bytes of data from 18 byte to 21th byte both inclusive 
        self.pulse_current_bytes = self.get_sta_output[18:22]
        # max pulse current data is 4 bytes of data from 22 byte to 25th byte both inclusive 
        self.max_pulse_current_bytes = self.get_sta_output[22:26]
        self.max_pulse_current_int = int.from_bytes(
            self.max_pulse_current_bytes, byteorder="little", signed=False
        )
        # bias current data is 4 bytes of data from 26 byte to 29th byte both inclusive 
        self.bias_current_bytes = self.get_sta_output[26:30]
        # max bias current data is 4 bytes of data from 30 byte to 33th byte both inclusive 
        self.max_bias_current_bytes = self.get_sta_output[30:34]
        self.max_bias_current_float = struct.unpack("<f", self.max_bias_current_bytes)[0]
        # softstart error data is 1 bytes of data, 34th byte 
        self.softstart_error_status = bin(self.get_sta_output[34])[2:] 
        #bin - convertes the byte into a binary
        #rjust is filling upto 2 bits
        self.softstart_error_status = self.softstart_error_status.rjust(8, '0')
        self.error_status = self.softstart_error_status[6]
        self.softstart_status = self.softstart_error_status[7]
    def get_ldd_trigger_settings(self):
        self.get_ldd_sta()
        return self.trigger_mode, self.trigger_edge, self.trigger_source
    def get_trigger_mode(self):
        self.get_ldd_trigger_settings()
        return self.trigger_mode 
    def get_trigger_edge(self):
        self.get_ldd_trigger_settings()
        return self.trigger_edge
    def get_trigger_source(self):
        self.get_ldd_trigger_settings()
        return self.trigger_source
    def get_capacitor_status():
        self.get_ldd_sta()
        return self.capacitor_status
    def get_connect_ldd(self):
        self.get_ldd_sta()
        return self.connection_status
    def get_ldd_chan(self):
        self.get_ldd_sta()
        return self.channel_status
    def get_ldd_trig(self):
        self.get_ldd_sta()
        return self.trigger_status
    def get_ldd_ctrl(self):
        self.get_ldd_sta()
        return self.ldd_ctrl_mode
    def get_ldd_freq(self):
        self.get_ldd_sta()
        self.frequency_float = struct.unpack("<f", self.frequency_bytes)[0]
        return self.frequency_float
    def get_ldd_pwid(self):
        self.get_ldd_sta()
        self.pulse_width_int = int.from_bytes(
            self.pulse_width_bytes, byteorder="little", signed=False
        )
        return self.pulse_width_int
    def get_ldd_pcur(self):
        self.get_ldd_sta()
        self.pulse_current_int = int.from_bytes(
            self.pulse_current_bytes, byteorder="little", signed=False
        )
        return self.pulse_current_int
    def get_ldd_bcur(self):
        self.get_ldd_sta()
        self.bias_current_float = struct.unpack("<f", self.bias_current_bytes)[0]
        return self.bias_current_float
    def get_ldd_softstart(self):
        self.get_ldd_sta()
        return self.softstart_status





    def get_pump_module_sta(self):
        self.pm_sta = self.get_parm("get_pm_sta")
        # returns 23 bytes last 17 bytes is data
        self.get_pm_sta_output = self.pm_sta[-17:]
        #pm temperature data is 4 bytes of data from 0 byte to 3rd byte both inclusive 
        self.pm_temperature_bytes = self.get_pm_sta_output[0:4]
        #pm humuduty data is 4 bytes of data from 4 byte to 7th byte both inclusive 
        self.pm_humidity_bytes = self.get_pm_sta_output[4:8]
        #pulse width data is 4 bytes of data from 8 byte to 12th byte both inclusive 
        self.pm_water_flow_bytes = self.get_pm_sta_output[8:12]
        #bin - convertes the byte into a binary
        #rjust is filling upto 6 bits
        self.pm_error_status = bin(ord(self.get_pm_sta_output[12:13]))[2:].rjust(8, '0')
        #pulse counter data is 4 bytes of data from 13th byte to 17th byte 
        self.pulse_counter_bytes = self.get_pm_sta_output[13:]
    
    def get_pump_module_temperature_float(self):
        self.get_pump_module_sta()
        self.pm_temperature_float = struct.unpack("<f", self.pm_temperature_bytes)[0]
        return self.pm_temperature_float
    
    def get_pump_module_humidity_float(self):
        self.get_pump_module_sta()
        self.pm_humidity_float = struct.unpack("<f", self.pm_humidity_bytes)[0]
        return self.pm_humidity_float
    
    def get_pump_module_water_flow_float(self):
        self.get_pump_module_sta()
        self.pm_water_flow_float = struct.unpack("<f", self.pm_water_flow_bytes)[0]
        return  self.pm_water_flow_float
    
    def get_pump_module_tcp_connection_error(self):
        self.get_pump_module_sta()
        self.tcp_connection_error = self.pm_error_status[2]
        return self.tcp_connection_error
    
    def get_pump_module_leakage_error(self):
        self.get_pump_module_sta()
        self.leakage_error = self.pm_error_status[3]
        return self.leakage_error
    
    def get_pump_module_forward_voltage_error(self):
        self.get_pump_module_sta()
        self.forward_voltage_error = self.pm_error_status[4]
        return self.forward_voltage_error
    
    def get_pump_module_temperature_error(self):
        self.get_pump_module_sta()
        self.temperature_error = self.pm_error_status[5]
        return self.temperature_error
    
    def get_pump_module_humidity_error(self):
        self.get_pump_module_sta()
        self.humidity_error = self.pm_error_status[6]
        return self.humidity_error
    
    def get_pump_module_water_flow_error(self):
        self.get_pump_module_sta()
        self.water_flow_error = self.pm_error_status[7]
        return self.water_flow_error
    
    def get_pump_module_pulse_counter_float(self):
        self.get_pump_module_sta()
        self.pulse_counter_float = struct.unpack("<f", self.pulse_counter_bytes)[0]
        return self.pulse_counter_float





    def get_amplifier_sta(self):
        self.amp_sta = self.get_parm("get_amp_sta")
        # returns 19 bytes last 13 bytes is data
        self.get_amp_sta_output = self.amp_sta[-13:]
        #amp base plate temperature data is 4 bytes of data from 0 byte to 3rd byte both inclusive 
        self.amp_base_plate_temp_bytes = self.get_amp_sta_output[0:4]
        #amp laser material temperature data is 4 bytes of data from 4 byte to 7th byte both inclusive 
        self.laser_material_temp_bytes = self.get_amp_sta_output[4:8]
        #amp vacuum pressure data is 4 bytes of data from 8 byte to 11th byte both inclusive 
        self.amp_vacuum_pressure_bytes = self.get_amp_sta_output[8:12]
        #amp error data is 1 bytes of data 12th byte
        self.amp_error_status = bin(ord(self.get_amp_sta_output[12:]))[2:]
        #bin - convertes the byte into a binary
        #rjust is filling upto 5 bits
        self.amp_error_status = self.amp_error_status.rjust(8, '0')
        self.base_plate_temperature_error = self.amp_error_status[7]
        self.laser_material_temperature_error = self.amp_error_status[6]
        self.amplifier_vacuum_error = self.amp_error_status[5]
        self.amplifier_operation_status = self.amp_error_status[4]
        self.amplifier_tcp_connection_error = self.amp_error_status[3]
    def get_amplifier_base_plate_temperature(self):
        self.get_amplifier_sta()
        self.amp_base_plate_temp_float = struct.unpack("<f", self.amp_base_plate_temp_bytes)[0]
        return self.amp_base_plate_temp_float
    def get_amplifier_laser_material_temperature(self):        
        self.laser_material_temp_float = struct.unpack("<f", self.laser_material_temp_bytes)[0]
        return self.laser_material_temp_float
    def get_amplifier_vacuum_pressure_float(self):
        self.amplifier_vacuum_pressure_float = struct.unpack("<f", self.amp_vacuum_pressure_bytes)[0]
        return self.amplifier_vacuum_pressure_float
    def get_amplifier_base_plate_temperature_error(self):
        self.get_amplifier_sta()
        return self.base_plate_temperature_error
    def get_amplifier_laser_material_temperature_error(self):
        self.get_amplifier_sta()
        return self.laser_material_temperature_error
    def get_amplifier_amplifier_vacuum_error(self):
        return self.amplifier_vacuum_error
    def get_amplifier_amplifier_tcp_connection_error(self):
        return self.amplifier_tcp_connection_error
    def get_amplifier_ctrl(self):
        self.get_amplifier_sta()
        return self.amplifier_operation_status





    def get_water_chiller_sta(self):
        self.water_chil_sta = self.get_parm("get_water_chil_sta")
        # returns 21 bytes last 15 bytes is data
        self.get_water_chil_sta_output = self.water_chil_sta[-15:]
        #water temperature data is 4 bytes of data from 0 byte to 3th byte both inclusive 
        self.water_chill_water_temperature_bytes = self.get_water_chil_sta_output[0:4]
        #water flow rate data is 4 bytes of data from 4 byte to 7th byte both inclusive 
        self.water_chill_water_flow_rate_bytes = self.get_water_chil_sta_output[4:8]
        #water chiller setpoint temperature data is 4 bytes of data from 8 byte to 11th byte both inclusive 
        self.water_chil_setpoint_temp_bytes = self.get_water_chil_sta_output[8:12]
        #water chiller operational status data is 1 byte of data 12th byte
        self.water_chiller_operational_status = bin(ord(self.get_water_chil_sta_output[12:13]))[2:].zfill(1)
        #water chiller error status data is 1 byte of data 13th byte
        self.water_chil_error_status = bin(ord(self.get_water_chil_sta_output[13:14]))[2:]
        #bin - convertes the byte into a binary
        #rjust is filling upto 8 bits
        self.water_chil_error_status =self.water_chil_error_status.rjust(8, '0')
        #water chiller 2 error status data is 1 byte of data 14th byte
        self.water_chil_error_status2 = bin(self.get_water_chil_sta_output[14])[2:]
        #bin - convertes the byte into a binary
        #rjust is filling upto 2 bits
        self.water_chil_error_status2 = self.water_chil_error_status2.rjust(8, '0')
    def get_water_chil_setpoint_temperature(self):
        self.get_water_chiller_sta()
        self.water_chil_setpoint_temp_float = struct.unpack("<f", self.water_chil_setpoint_temp_bytes)[0]
        return self.water_chil_setpoint_temp_float
    def get_chil_ctrl(self):
        self.get_water_chiller_sta()
        return self.water_chiller_operational_status
    def get_water_chil_water_flow_rate(self):
        self.get_water_chiller_sta()
        self.water_chill_water_flow_rate_float = struct.unpack("<f", self.water_chill_water_flow_rate_bytes)[0]
    def get_water_chil_water_temperature(self):
        self.get_water_chiller_sta()
        self.water_chill_water_temperature_float = struct.unpack("<f", self.water_chill_water_temperature_bytes)[0]







    def get_interlock_sta(self):
        self.interlock_sta = self.get_parm("get_interlock_sta")
        self.interlock_status_output = bin(ord(self.interlock_sta[-1:]))[2:]
        #bin - convertes the byte into a binary
        #rjust is filling upto 6 bits
        self.interlock_status_output = self.interlock_status_output.rjust(8, '0')
        print("self.interlock_status_output",self.interlock_status_output)
        self.interlock_pump_module_error = self.interlock_status_output[7]
        self.interlock_water_cooling_error = self.interlock_status_output[6]
        self.interlock_amp_ctrl_error = self.interlock_status_output[5]
        self.interlock_external_error = self.interlock_status_output[4]
        self.interlock_reset_required = self.interlock_status_output[3]
        self.interlock_tcp_connection_error = self.interlock_status_output[2]


    def get_image_data(self):
        str1 = self._command_dict["get_image"]
        self.socket.send(str1)
        #size of the data that will be returned is 2457606, so the recv parameter size is set to 3000000
        self.image_data = self.socket.recv(3000000)
        time.sleep(config.long_wait)
        print("Wait time to Get Image:", config.long_wait)
        self.image_data_output = self.image_data[6:]
        self.length_of_image_data_1D = len(self.image_data_output)
        return self.length_of_image_data_1D

    def get_histogram_data(self):
        str1 = self._command_dict["get_histogram"]
        self.socket.send(str1)
        #size of the data that will be returned is 4102, so the recv parameter size is set to 5000
        self.histogram_data = self.socket.recv(5000)
        time.sleep(config.long_wait)
        print("Wait time to Get Histogram Data:", config.long_wait)
        self.histogram_data_output = self.histogram_data[6:] #
        self.length_of_histogram_data_1D = len(self.histogram_data_output)
        return self.length_of_histogram_data_1D

    def set_connection(self, parameter_name):
        str1 = (
            self._command_dict[parameter_name]
        )
        self.socket.send(str1)
        #print(self.socket.recv(1024))
        #using the standard recv size of 1024
        self.socket.recv(1024)



    def set_parm(self, parameter_name, set_value):
        str1 = (
            self._command_dict[parameter_name] + set_value
        )  # appending command with the set value
        print("command to set " + parameter_name + " str1 - " + str(set_value))
        number_of_bytes_sent = self.socket.send(str1)
        print("number_of_bytes_sent = ",number_of_bytes_sent)
        #print(self.socket.recv(1024))
        #using the standard recv size of 1024
        return self.socket.recv(1024)
    def get_parm(self, paramater_name):
        str1 = self._command_dict[paramater_name]
        #print("command to get ",str1)
        self.socket.send(str1)
        #using the standard recv size of 1024
        returnvar = self.socket.recv(1024)
        #print(returnvar)
        return returnvar



    def PreRequsites_to_set_ldd_parameters_ON(self):
        if (
            self.ldd_ctrl_mode == STANDBY
        ):
            self.set_ldd_ctrl(ON)#prerequisite for trigger
        if (
            self.trigger_status == TurnedOff
        ):
           self.set_ldd_trig(ON)#prerequisite for channel
        if (
            self.channel_status == TurnedOff
        ):
            self.set_ldd_chan(ON)

    def PreRequsites_to_set_ldd_parameters_OFF(self):
        if (
            self.channel_status == TurnedOn
        ):
            self.set_ldd_chan(OFF)
        if (
            self.trigger_status == TurnedOn
        ):
           self.set_ldd_trig(OFF)
        if (
            self.ldd_ctrl_mode == OPERATIONAL
        ):
            self.set_ldd_ctrl(OFF)
        

if __name__ == "__main__":
    Lastronics = LastronicsLaserAmplifierPreAmp2(macros_device_ip, macros_device_port)
    Lastronics.set_ldd_ctrl(ON)
    print(Lastronics.status)
    print(Lastronics.get_ldd_ctrl())
    Lastronics.set_ldd_ctrl(OFF)
    print(Lastronics.status)
    print(Lastronics.get_ldd_ctrl())
    # print(Lastronics.ldd_ctrl_mode)
    # print("turning on trigger")
    # Lastronics.set_ldd_trig(ON)
    # print(Lastronics.status)
    # print(Lastronics.trigger_status)
    #  print("turning on channel")
    # Lastronics.set_ldd_chan(ON)
    # print(Lastronics.status)
    # print(Lastronics.channel_status)
    # print("single")  
    # Lastronics.set_ldd_trigger_Continuous_single(Single)
    # print(Lastronics.status)
    # print("Positive")
    # Lastronics.set_ldd_trigger_positive_negative(Positive)
    # print(Lastronics.status)
    # print("External")
    # Lastronics.set_ldd_trigger_internal_external(External)
    # print(Lastronics.status)
    # print("continues")
    # Lastronics.set_ldd_trigger_Continuous_single(Continuous)
    # print(Lastronics.status)
    # print("Negative")
    # Lastronics.set_ldd_trigger_positive_negative(Negative)
    # print(Lastronics.status)
    # print("Internal")
    # Lastronics.set_ldd_trigger_internal_external(Internal)
    # print(Lastronics.status)
    # Lastronics.set_ldd_trig(OFF)
    # print(Lastronics.status)
    # print(Lastronics.trigger_status)
    # Lastronics.set_ldd_ctrl(OFF)
    # print(Lastronics.status)
    # print(Lastronics.ldd_ctrl_mode)
    # Lastronics.set_amplifier_target_temperature(30)