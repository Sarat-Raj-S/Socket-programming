######   Device Parameters   ######

device_ip = "10.2.3.1"
device_port = 14601



#####   Wait Time For Parameters in Seconds   ######

wait_to_set_laser_diode_driver_control_to_operational_or_standby = 26.0 # The default delay time for standby or operate is 25 seconds as per data sheet
wait_to_set_laser_diode_driver_trigger_on_off = 10.0
wait_to_set_laser_diode_driver_channel_status_on_off = 10.0
wait_time_to_set_trigger_setting = 11.0
short_wait = 5.0 # 5 seconds for device to respond 
medium_wait = 15.0
long_wait = 30.0


#####   Set Values of Parameters for Testing   ######
### on parameters and off parameters must not be same  ###


driver_pulse_current_set_value_when_pre_on = [(10,10),(20,20)] #in Amp
driver_pulse_current_set_value_when_pre_off = [(11,11),(21,21)] #in Amp
driver_bias_current_set_value_when_pre_on = [(1.0,1.0),(2.0,2.0)] #in Amp
driver_bias_current_set_value_when_pre_off = [(1.1,1.1),(2.1,2.1)] #in Amp
driver_frequency_set_value_when_pre_on = [(10.0,10.0),(20.0,20.0)] #in Hertz
driver_frequency_set_value_when_pre_off = [(15.0,15.1),(25.1,25.1)] #in Hertz
driver_pulse_width_set_value_when_pre_on = [(201,201),(300,300)]
driver_pulse_width_set_value_when_pre_off = [(250,250),(259,259)]
chiller_setpoint_temperature_set_value = [(19.0,19.0),(25.0,25.0)] #in °C, use other than 0.0
amplifier_target_temperature_set_value_when_ctrl_on = [(30.0,30.0),(20.0,20.0)] #in °C
set_amplifier_target_temperature = [(5.1,5.1),(7.1,7.1)] #in °C
spa_divider_set_value = [(1,1),(2,2)]
spa_gain_raw_set_value = [(1,1),(2,2)]
spa_black_level_set_value = [(1.0,1.0),(2.0,2.0)]
spa_trigger_delay_absloute_set_value = [(1.0,1.0),(2.0,2.0)] #in mS
spa_exposure_time_absloute_set_value = [(1.0,1.0),(2.0,2.0)] #in mS
spa_n_background_averages_set_value = [(1.0,1.0),(2.0,2.0)] #in mS
spa_number_of_ticks_in_legend_set_value = [(1.0,1.0),(2.0,2.0)] #in mS
spa_image_averages_set_value = [(1.0,1.0),(2.0,2.0)] #in mS 
spa_energy_claibration_factor_set_value = [(1.0,1.0),(2.0,2.0)] #(setting, expected) in mJ  
spa_ROI_far_field_set_value = [(1.0,1.0,2.0,1.0,1.0,2.0),(2.0,2.0,4.0,2.0,2.0,4.0)] #(setting, expected) in mJ  
spa_ROI_near_field_set_value = [(1.0,1.0,2.0,1.0,1.0,2.0),(2.0,2.0,4.0,2.0,2.0,4.0)] #(setting, expected) in mJ  
spa_far_field_reference_set_value = [(1.0,1.0,1.0,1.0),(2.0,2.0,2.0,2.0)] #(setting, expected) in mJ  
spa_near_field_reference_set_value = [(1.0,1.0,1.0,1.0),(2.0,2.0,2.0,2.0)] #(setting, expected) in mJ  
spa_gauss_order_set_value = [(10.0, 10.0),(20.0, 20.0)]
spa_HWB_set_value = [(10.0, 10.0),(20.0, 20.0)]


#####   Tolerance Limits for Values Parameters   ######

chiller_setpoint_temperature_tolerance = 5 #in °C
driver_frequency_tolerance = 1 #in Hertz
driver_pulse_current_tolerance = 0.5 #in Amp
driver_bias_current_tolerance = 0.05 #in Amp
driver_pulse_width_tolerance = 5 #in µs
spa_energy_tolerance = 5 #in µJ
amplifier_target_temperature_tolerance = 5 #in °C
spa_far_field_X_centroid_tolerance = 5
spa_far_field_Y_centroid_tolerance = 5
spa_near_field_X_centroid_tolerance = 5
spa_near_field_Y_centroid_tolerance = 5
spa_far_field_delta_X_centroid_tolerance = 5
spa_far_field_delta_Y_centroid_tolerance = 5
spa_near_field_delta_X_centroid_tolerance = 5
spa_near_field_delta_Y_centroid_tolerance = 5

#####   Get Values of Parameters   ######

spa_energy_expected = [(5)] #in µJ
spa_far_field_XY_centroid_expected = [(25.0,35.0),(54.0,2.0)]#(X value, Y Value)
spa_near_field_XY_centroid_expected = [(25.0,35.0),(54.0,2.0)]#(X value, Y Value)
spa_far_field_delta_XY_centroid_expected = [(25.0,35.0),(54.0,2.0)]#(ΔX value, ΔY Value)
spa_near_field_delta_XY_centroid_expected = [(25.0,35.0),(54.0,2.0)]#(ΔX value, ΔY Value)
spa_defined_image_size = 2457600
spa_defined_histogram_size = 4096

pump_module_temperature_min_allowable_value = 0#in °C
pump_module_temperature_max_allowable_value = 100#in °C
pump_module_relative_humidity_min_allowable_value = 0#in %
pump_module_relative_humidity_max_allowable_value = 100#in %
pump_module_water_flow_min_allowable_value = 0 #in L/min #check the manual for normal fow rate
pump_module_water_flow_max_allowable_value = 100 #in L/min #check the manual for normal fow rate
pump_module_pulse_count_min_allowable_value = 0
pump_module_pulse_count_max_allowable_value = 2000000000
amplifier_base_plate_temperature_expected_max_allowable_value = 100 #in °C
amplifier_base_plate_temperature_expected_min_allowable_value = 0 #in °C
amplifier_laser_material_temperature_expected_max_allowable_value = 100 #in °C
amplifier_laser_material_temperature_expected_min_allowable_value = 0 #in °C
amplifier_vacuum_pressure_expected_max_allowable_value = 100 #in mbar
amplifier_vacuum_pressure_expected_min_allowable_value = 0 #in mbar
water_chill_water_flow_rate_min_allowable_value = 0
water_chill_water_flow_rate_max_allowable_value = 100
water_chill_water_temperature_min_allowable_value = 0
water_chill_water_temperature_max_allowable_value =  50
