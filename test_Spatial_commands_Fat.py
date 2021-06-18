# def test_WHEN_spa_spatial_divider_is_set_to_setting_THEN_check_spatial_divider_is_expected():
#     set_value = 10
#     spa_divider_bytes = socket.send("set_spa_divider" + set_value.to_bytes(length=4, byteorder="little", signed=False))
#     return_value = socket.revieve(100)
#     print("wait time to set Spatial Divider is ",5, return_value[])
#     time.sleep(5)
#     get_spatial_divider(spa_divider_bytes[-4:]) 
#     spa_divider = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#     assert_that(preamp2.spa_divider, is_(expected))

# def test_WHEN_spa_spatial_gain_is_set_to_setting_THEN_check_spatial_gain_is_expected():
#         set_value = 10
#         spa_gain_bytes = socket.send("set_spa_gain", set_value.to_bytes(length=4, byteorder="little", signed=False))
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Gain is ",5, return_value[])
#         time.sleep(5)
#         get_spatial_gain(spa_gain_bytes[-4:])
#         spa_gain = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#     preamp2.set_spatial_gain(setting)
#     assert_that(preamp2.spa_gain, is_(expected))
    

# def test_WHEN_spa_spatial_black_level_is_set_to_setting_THEN_check_spatial_black_level_is_expected():
#         set_value = 10
#         spa_black_level_gain_bytes = socket.send("set_spa_black_lvl_gain", set_value.to_bytes(length=4, byteorder="little", signed=False))
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Black Level Gain is ",5, return_value[])
#         time.sleep(5)
#         get_spatial_black_level_gain(spa_black_level_gain_bytes[-4:])
#         spa_black_level_gain = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#     preamp2.set_spatial_black_level_gain(setting)
#     assert_that(preamp2.spa_black_level_gain, is_(expected))

# def test_WHEN_spa_spatial_trigger_mode_is_set_to_0_THEN_check_spatial_trigger_mode_is_turned_OFF(preamp2):
#         set_value = set_value.to_bytes(length=4, byteorder="little", signed=False)
#         spa_trigger_mode_bytes = socket.send("set_spa_trig_mode", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Trigger Mode is ",5, return_value[])
#         time.sleep(5)
#         get_spatial_trigger_mode(spa_trigger_mode_bytes[-4:])
#         spa_trigger_mode = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#     preamp2.set_spatial_trigger_mode(0)
#     assert preamp2.spa_trigger_mode == Trigger_Off 

# def test_WHEN_spa_spatial_trigger_mode_is_set_to_1_THEN_check_spatial_trigger_mode_is_turned_ON(preamp2):
#         set_value = set_value.to_bytes(length=4, byteorder="little", signed=False)
#         spa_trigger_source_bytes = socket.send("set_spa_trig_src", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Trigger Source is ",5, return_value[])
#         time.sleep(5)
#         get_spatial_trigger_source(spa_trigger_source_bytes[-4:])
#         spa_trigger_source = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#     preamp2.set_spatial_trigger_mode(1)
#     assert preamp2.spa_trigger_mode == Trigger_On

# def test_WHEN_spa_spatial_trigger_source_is_set_to_0_THEN_check_spatial_trigger_source_is_in_SOFTWARE(preamp2):
#         set_value = set_value.to_bytes(length=4, byteorder="little", signed=False)
#         spa_trigger_edge_bytes = socket.send("set_spa_trig_edge", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Trigger Edge is ",5, return_value[])
#         time.sleep(5)
#         get_spatial_trigger_edge(spa_trigger_edge_bytes[-4:])
#         spa_trigger_edge = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#     preamp2.set_spatial_trigger_source(0)
#     assert preamp2.spa_trigger_source == Software 

# def test_WHEN_spa_spatial_trigger_source_is_set_to_line_1_THEN_check_spatial_trigger_source_is_in_LINE_1(preamp2):
#     preamp2.set_spatial_trigger_source(line1)
#     assert preamp2.spa_trigger_source == line_1

# def test_WHEN_spa_spatial_trigger_source_is_set_to_line_2_THEN_check_spatial_trigger_source_is_in_LINE_2(preamp2):
#     preamp2.set_spatial_trigger_source(line2)
#     assert preamp2.spa_trigger_source == line_2

# def test_WHEN_spatial_trigger_edge_command_is_set_to_ON_THEN_spatial_trigger_edge_is_POSITIVE_edge(preamp2):
#     preamp2.set_spatial_trigger_edge(ON)
#     assert preamp2.spa_trigger_edge == Positive 

# def test_WHEN_spatial_trigger_edge_command_is_set_to_OFF_THEN_spatial_trigger_edge_is_NEGATIVE_edge(preamp2):
#     preamp2.set_spatial_trigger_edge(OFF)
#     assert preamp2.spa_trigger_edge == Negative


# def test_WHEN_spatial_trigger_delay_absolute_command_is_set_to_setting_value_THEN_spatial_trigger_delay_absolute_is_expected():
#         if (set_value <= 0.0 and set_value <= 1000.0):
#             set_value = struct.pack("<d", set_value)
#             spa_trigger_delay_absloute_bytes = socket.send("set_spa_trig_delay", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Trigger Delay Absolute is ",5, return_value[])
#         time.sleep(5)
#         get_spatial_trigger_delay_absloute(spa_trigger_delay_absloute_bytes[-8:])
#         spa_trigger_delay_absloute = struct.unpack("<d", get_value_bytes)
#     preamp2.set_spatial_trigger_delay_absloute(setting)
#     assert_that(preamp2.spa_trigger_delay_absloute, is_(expected)) 
    

# def test_WHEN_spatial_exposure_time_absolute_command_is_set_to_setting_value_THEN_spatial_exposure_time_absolute_is_expected():
#         if (set_value <= 0.02 and set_value <= 10000.0):             
#             set_value = struct.pack("<d", set_value) #specifying double since 8 bytes needed to be sent
#             spa_exposure_time_absloute_bytes = socket.send("set_spa_expos_time", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Exposure Time Absolute is ",5, return_value[])
#         time.sleep(5)
#         get_spatial_exposure_time_absloute(spa_exposure_time_absloute_bytes[-8:])
#         spa_exposure_time_absloute = struct.unpack("<d", get_value_bytes)
#     preamp2.set_spatial_exposure_time_absloute(setting)
#     assert_that(preamp2.spa_exposure_time_absloute, is_(expected)) 

# def test_WHEN_spatial_save_background_command_is_set_to_ON_THEN_spatial_save_background_is_save(preamp2):
#         spa_save_background = socket.send("set_spa_save_backgnd", set_value)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Save Background is ",5, return_value[])
#         time.sleep(5)
#         spa_save_background_return_val = spa_save_background[-1:] # store the last byte of ack from the device
#     preamp2.set_spa_save_background(ON)
#     assert preamp2.spa_save_background_return_val == Save

# def test_WHEN_spatial_save_background_command_is_set_to_OFF_THEN_spatial_save_background_is_OFF(preamp2):
#     preamp2.set_spa_save_background(OFF)
#     assert preamp2.spa_save_background_return_val == IsOff

# def test_WHEN_spatial_substract_background_command_is_set_to_ON_THEN_spatial_substract_background_is_substract(preamp2):
#     spa_sub_background = socket.send("set_spa_sub_backgnd", set_value)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Substract Background is ",5, return_value[])
#         time.sleep(5)
#         spa_substract_background_return_val = spa_sub_background[-1:] # store the last byte of ack (\x00 or \x01) from the device
#     preamp2.set_spa_substract_background(ON)
#     assert preamp2.spa_substract_background_return_val == Substract

# def test_WHEN_spatial_substract_background_command_is_set_to_OFF_THEN_spatial_substract_background_is_off(preamp2):
#     preamp2.set_spa_substract_background(OFF)
#     assert preamp2.spa_substract_background_return_val == IsOff


# def test_WHEN_spatial_N_background_averages_command_is_set_to_setting_THEN_spatial_n_background_averages_is_as_expected():
#         set_value = 10 
#         socket.send("set_spa_n_backgnd_avgs", set_value.to_bytes(length=4, byteorder="little", signed=False))
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Background Averages is ",5, return_value[])
#         time.sleep(5)
#         spa_n_backgnd_avgs = get_parm("get_spa_n_backgnd_avgs_done")
#         spa_n_backgnd_avgs_return_val_bytes = spa_n_backgnd_avgs[-4:]
#         spa_n_backgnd_avgs_return_val = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#     preamp2.set_spa_N_background_averages(setting)
#     assert preamp2.spa_n_backgnd_avgs_return_val == expected

# def test_WHEN_spatial_number_of_ticks_in_legend_command_is_set_to_setting_THEN_spatial_number_of_ticks_in_legend_is_as_expected():
#     preamp2.set_spa_number_of_ticks_in_ledgend(setting)
#     assert preamp2.spa_number_of_ticks_in_ledgend_return_val == expected


# def test_WHEN_spatial_adjustments_mode_command_is_set_to_ON_THEN_spatial_adjustments_mode_is_ON(preamp2):
#     preamp2.set_spa_adjustments_mode(ON)
#     assert preamp2.spa_adjustments_mode_return_val == IsOn

# def test_WHEN_spatial_adjustments_mode_command_is_set_to_OFF_THEN_spatial_adjustments_mode_is_OFF(preamp2):
#     preamp2.set_spa_adjustments_mode(OFF)
#     assert preamp2.spa_adjustments_mode_return_val == IsOff

# def test_WHEN_spatial_image_averages_command_is_set_to_setting_THEN_spatial_image_averages_is_as_expected():
#     preamp2.set_spa_image_averages(setting)
#     assert preamp2.spa_image_average_return_val == expected

# def test_spatial_n_pictures_in_stack_is_as_expected(preamp2):
#     preamp2.get_spa_N_pictures_in_stack()
#     assert preamp2.spa_n_backgnd_avgs_return_val == expected

# def test_WHEN_spatial_camera_standard_properties_command_is_set_to_ON_THEN_spatial_camera_standard_properties_is_ON(preamp2):
#     preamp2.set_spa_camera_standard_properties(ON)
#     assert preamp2.spa_cam_standard_properties_return_val == IsOn

# def test_WHEN_spatial_camera_standard_properties_command_is_set_to_OFF_THEN_spatial_camera_standard_properties_is_OFF(preamp2):
#     preamp2.set_spa_camera_standard_properties(OFF)
#     assert preamp2.spa_cam_standard_properties_return_val == IsOff

# def test_spatial_far_field_XY_centroid_is_as_expected(preamp2, expected_X_VALUE, expected_Y_VALUE):
#     preamp2.get_spa_far_field_XY_centroid()
#     assert_that(preamp2.spa_far_field_X_centroid_return_value, is_(close_to(expected_X_VALUE, config.spa_far_field_X_centroid_tolerance)))
#     assert_that(preamp2.spa_far_field_Y_centroid_return_value, is_(close_to(expected_Y_VALUE, config.spa_far_field_Y_centroid_tolerance)))


# def test_spatial_near_field_XY_centroid_is_as_expected(preamp2, expected_X_VALUE, expected_Y_VALUE):
#     preamp2.get_spa_near_field_XY_centroid()
#     assert_that(preamp2.spa_near_field_X_centroid_return_value, is_(close_to(expected_X_VALUE, config.spa_near_field_X_centroid_tolerance)))
#     assert_that(preamp2.spa_near_field_Y_centroid_return_value, is_(close_to(expected_Y_VALUE, config.spa_near_field_Y_centroid_tolerance)))

# def test_spatial_far_field_delta_XY_centroid_is_as_expected(preamp2, expected_X_VALUE, expected_Y_VALUE):
#     preamp2.get_spa_far_field_DELTA_XY_centroid()
#     assert_that(preamp2.spa_far_field_delta_X_centroid_return_value, is_(close_to(expected_X_VALUE, config.spa_far_field_delta_X_centroid_tolerance)))
#     assert_that(preamp2.spa_far_field_delta_Y_centroid_return_value, is_(close_to(expected_Y_VALUE, config.spa_far_field_delta_Y_centroid_tolerance)))


# def test_spatial_near_field_delta_XY_centroid_is_as_expected(preamp2, expected_X_VALUE, expected_Y_VALUE):
#     preamp2.get_spa_NEAR_field_DELTA_XY_centroid()
#     assert_that(preamp2.spa_near_field_delta_X_centroid_return_value, is_(close_to(expected_X_VALUE, config.spa_near_field_delta_X_centroid_tolerance)))
#     assert_that(preamp2.spa_near_field_delta_Y_centroid_return_value, is_(close_to(expected_Y_VALUE, config.spa_near_field_delta_Y_centroid_tolerance)))

# def test_spatial_energy_is_as_expected(preamp2, expected):
#     preamp2.get_spa_energy()
#     assert_that(preamp2.spa_energy_return_value, is_(expected)) 


# def test_spatial_energy_calibration_factor_is_as_expected():
#     preamp2.set_spa_energy_calibration_factor(setting)
#     assert preamp2.spa_energy_calibration_factor_return_val == expected


# def test_WHEN_spatial_roi_near_field_command_is_set_to_setting_THEN_spatial_roi_near_field_X_Y_and_Rad_is_as_expected(preamp2, X_VALUE, Y_VALUE, RAD_VALUE, expected_X_VALUE, expected_Y_VALUE, expected_RAD_VALUE):
#     preamp2.set_spa_ROI_near_field(X_VALUE,Y_VALUE,RAD_VALUE)
#     assert preamp2.spa_ROI_near_field_x_return_val == expected_X_VALUE
#     assert preamp2.spa_ROI_near_field_y_return_val == expected_Y_VALUE
#     assert preamp2.spa_ROI_near_field_rad_return_val == expected_RAD_VALUE


# def test_WHEN_spatial_roi_far_field_command_is_set_to_setting_THEN_spatial_roi_far_field_X_Y_and_Rad_is_as_expected(preamp2, X_VALUE, Y_VALUE, RAD_VALUE, expected_X_VALUE, expected_Y_VALUE, expected_RAD_VALUE):
#     preamp2.set_spa_ROI_far_field(X_VALUE,Y_VALUE,RAD_VALUE)
#     assert preamp2.spa_ROI_far_field_x_return_val == expected_X_VALUE
#     assert preamp2.spa_ROI_far_field_y_return_val == expected_Y_VALUE
#     assert preamp2.spa_ROI_far_field_rad_return_val == expected_RAD_VALUE
    

# def test_WHEN_spatial_near_field_reference_command_is_set_to_setting_THEN_spatial_near_field_reference_X_Y_is_as_expected(preamp2, X_VALUE, Y_VALUE, expected_X_VALUE, expected_Y_VALUE):
#     preamp2.set_spa_near_field_reference(X_VALUE,Y_VALUE,RAD_VALUE)
#     assert_that(preamp2.spa_near_field_reference_x_return_val, is_(expected_X_VALUE))
#     assert_that(preamp2.spa_near_field_reference_y_return_val, is_(expected_Y_VALUE))

    

# def test_WHEN_spatial_far_field_reference_command_is_set_to_setting_THEN_spatial_far_field_reference_X_Y_is_as_expected(preamp2, X_VALUE, Y_VALUE, expected_X_VALUE, expected_Y_VALUE):
#     preamp2.set_spa_far_field_reference(X_VALUE,Y_VALUE,RAD_VALUE)
#     assert_that(preamp2.spa_far_field_reference_x_return_val, is_(expected_X_VALUE))
#     assert_that(preamp2.spa_far_field_reference_y_return_val, is_(expected_Y_VALUE))


# def test_WHEN_spatial_gauss_order_command_is_set_to_setting_THEN_spatial_gauss_order_is_as_expected():
#     preamp2.set_spa_gauss_order(setting)
#     assert preamp2.spa_gauss_order_return_val == expected

# def test_WHEN_spatial_HWB_command_is_set_to_setting_THEN_spatial_HWB_is_as_expected():
#     preamp2.set_spa_HWB(setting)
#     assert preamp2.spa_HWB_return_val == expected

# def test_WHEN_spatial_image_is_get_THEN_image_received_size_is_correct(preamp2):
#     preamp2.get_image_data()
#     assert preamp2.length_of_image_data_1D == config.spa_defined_image_size

# def test_WHEN_spatial_histogram_is_get_THEN_histogram_received_size_is_correct(preamp2):
#     preamp2.get_histogram_data()
#     assert preamp2.length_of_histogram_data_1D == config.spa_defined_histogram_size


#     def set_spa_number_of_ticks_in_ledgend(self, set_value):
#         set_value = set_value.to_bytes(length=4, byteorder="little", signed=False)
#         spa_number_of_ticks_in_ledgend_bytes = socket.send("set_spa_n_backgnd_avgs", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Number of Ticks in Ledgend is ",5, return_value[])
#         time.sleep(5)
#         get_spa_number_of_ticks_in_ledgend(spa_number_of_ticks_in_ledgend_bytes[-4:])
#     def get_spa_number_of_ticks_in_ledgend(self,get_value_bytes):
#         spa_number_of_ticks_in_ledgend_return_val = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#         return spa_number_of_ticks_in_ledgend_return_val

#     def set_spa_adjustments_mode(self, set_value):
#         spa_adjustments_mode = socket.send("set_spa_adjustments_mode", set_value)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Adjustments Mode is ",5, return_value[])
#         time.sleep(5)
#         spa_adjustments_mode_return_val = spa_adjustments_mode[-1:]

#     def set_spa_image_averages(self, set_value):
#         set_value = set_value.to_bytes(length=4, byteorder="little", signed=False)
#         spa_image_average_bytes = socket.send("set_images_avg", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Images Averages is ",5, return_value[])
#         time.sleep(5)
#         get_spa_image_averages(spa_image_average_bytes[-4:])
#     def get_spa_image_averages(self,get_value_bytes):
#         spa_image_average_return_val = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#         return spa_image_average_return_val

#     def get_spa_N_pictures_in_stack(self):
#         spa_N_pictures_in_stack = get_parm("get_spa_n_backgnd_avgs_done")
#         spa_N_pictures_in_stack_return_val_bytes = spa_N_pictures_in_stack[-4:]
#         spa_N_pictures_in_stack_return_val = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#         return spa_n_backgnd_avgs_return_val

#     def set_spa_camera_standard_properties(self, set_value):
#         spa_cam_standard_properties = socket.send("set_spa_cam_standard_properties", set_value)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Camera Standard Properties is ",5, return_value[])
#         time.sleep(5)
#         spa_cam_standard_properties_return_val = spa_cam_standard_properties[-1:] # store the last byte of ack from the device

#     def get_spa_far_field_XY_centroid(self):
#         spa_far_field_XY_centroid = get_parm("get_spa_far_field_xy_centroid")
#         spa_far_field_XY_centroid_return_value = struct.unpack("<d", spa_far_field_XY_centroid)
#         spa_far_field_X_centroid_return_value = spa_far_field_XY_centroid_return_value[0:4]
#         spa_far_field_Y_centroid_return_value = spa_far_field_XY_centroid_return_value[4:]
#         return spa_far_field_X_centroid_return_value,spa_far_field_Y_centroid_return_value

#     def get_spa_near_field_XY_centroid(self):
#         spa_near_field_XY_centroid = get_parm("get_spa_near_field_xy_centroid")
#         spa_near_field_XY_centroid_return_value = struct.unpack("<d", spa_near_field_XY_centroid)
#         spa_near_field_X_centroid_return_value = spa_near_field_XY_centroid_return_value[0:4]
#         spa_near_field_Y_centroid_return_value = spa_near_field_XY_centroid_return_value[4:]
#         return spa_near_field_X_centroid_return_value,spa_near_field_Y_centroid_return_value

#     def get_spa_far_field_delta_XY_centroid(self):
#         spa_far_field_delta_XY_centroid = get_parm("get_spa_far_field_delta_xy_centroid")
#         spa_far_field_delta_XY_centroid_return_value = struct.unpack("<d", spa_far_field_delta_XY_centroid)
#         spa_far_field_delta_X_centroid_return_value = spa_far_field_delta_XY_centroid_return_value[0:4]
#         spa_far_field_delta_Y_centroid_return_value = spa_far_field_delta_XY_centroid_return_value[4:]
#         return spa_far_field_delta_X_centroid_return_value,spa_far_field_delta_Y_centroid_return_value

#     def get_spa_near_field_delta_XY_centroid(self):
#         spa_near_field_delta_XY_centroid = get_parm("get_spa_near_field_delta_xy_centroid")
#         spa_near_field_delta_XY_centroid_return_value = struct.unpack("<d", spa_near_field_delta_XY_centroid)
#         spa_near_field_delta_X_centroid_return_value = spa_near_field_delta_XY_centroid_return_value[0:4]
#         spa_near_field_delta_Y_centroid_return_value = spa_near_field_delta_XY_centroid_return_value[4:]
#         return spa_near_field_delta_X_centroid_return_value,spa_near_field_delta_Y_centroid_return_value

#     def get_spa_energy(self):
#         spa_energy = get_parm("get_spa_energy")
#         spa_energy_return_value = struct.unpack("<f", spa_energy)
#         return spa_energy_return_value

#     def set_spa_energy_calibration_factor(self, set_value):
#         set_value = struct.pack("<f", set_value)
#         spa_energy_calibration_factor = socket.send("set_spa_energy_calib_factor", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Energy Calibration Factor is ",5, return_value[])
#         time.sleep(5)
#         get_spa_energy_calibration_factor(spa_energy_calibration_factor[-4:])
#     def get_spa_energy_calibration_factor(self,get_value_bytes):
#         spa_energy_calibration_factor_return_val = struct.unpack("<d", get_value_bytes)
#         return spa_energy_calibration_factor_return_val

#     def set_spa_ROI_near_field(self, set_x_value, set_y_value, set_rad_value):
#         set_x_value_bytes = set_x_value.to_bytes(
#         length=4, byteorder="little", signed=False
#         )
#         set_y_value_bytes = set_y_value.to_bytes(
#         length=4, byteorder="little", signed=False
#         )
#         set_radian_value_bytes = set_rad_value.to_bytes(
#         length=4, byteorder="little", signed=False
#         )
#         set_value = set_x_value_bytes + set_y_value_bytes + set_radian_value_bytes
#         set_value = set_value.to_bytes(
#         length=12, byteorder="little", signed=False
#         )
#         spa_ROI_near_field_bytes = socket.send("set_spa_roi_near_field", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial ROI near Field is ",5, return_value[])
#         time.sleep(5)
#         get_spa_ROI_near_field(spa_ROI_near_field_bytes[-12:])
#     def get_spa_ROI_near_field(self,get_value_bytes):
#         get_x_value_bytes = get_value_bytes[0:4]
#         get_y_value_bytes = get_value_bytes[4:8]
#         get_rad_value_bytes = get_value_bytes[8:]
#         spa_ROI_near_field_x_return_val = int.from_bytes(
#             get_x_value_bytes, byteorder="little", signed=False
#         )
#         spa_ROI_near_field_y_return_val = int.from_bytes(
#             get_y_value_bytes, byteorder="little", signed=False
#         )
#         spa_ROI_near_field_rad_return_val = int.from_bytes(
#             get_rad_value_bytes, byteorder="little", signed=False
#         )
#         return spa_ROI_near_field_x_return_val,spa_ROI_near_field_y_return_val,spa_ROI_near_field_rad_return_val

#     def set_spa_ROI_far_field(self, set_x_value, set_y_value, set_rad_value):
#         set_x_value_bytes = set_value.to_bytes(length=4, byteorder="little", signed=False)
#         set_y_value_bytes = set_value.to_bytes(length=4, byteorder="little", signed=False)
#         set_radian_value_bytes = set_value.to_bytes(length=4, byteorder="little", signed=False)
#         set_value = set_x_value_bytes + set_y_value_bytes + set_radian_value_bytes
#         spa_ROI_far_field_bytes = socket.send("set_spa_roi_far_field", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial ROI far Field is ",5, return_value[])
#         time.sleep(5)
#         get_spa_ROI_far_field(spa_ROI_far_field_bytes[-12:])
#     def get_spa_ROI_far_field(self,get_value_bytes):
#         get_x_value_bytes = get_value_bytes[0:4]
#         get_y_value_bytes = get_value_bytes[4:8]
#         get_rad_value_bytes = get_value_bytes[8:]
#         spa_ROI_far_field_x_return_val = int.from_bytes(
#             get_x_value_bytes, byteorder="little", signed=False
#         )
#         spa_ROI_far_field_y_return_val = int.from_bytes(
#             get_y_value_bytes, byteorder="little", signed=False
#         )
#         spa_ROI_far_field_rad_return_val = int.from_bytes(
#             get_rad_value_bytes, byteorder="little", signed=False
#         )
#         return spa_ROI_far_field_x_return_val, spa_ROI_far_field_y_return_val, spa_ROI_far_field__return_val

#     def set_spa_far_field_reference(self, set_x_value, set_y_value):
#         set_x_value_bytes = struct.pack("<f", set_x_value)
#         set_y_value_bytes = struct.pack("<f", set_y_value)
#         set_value = set_x_value_bytes + set_y_value_bytes 
#         spa_far_field_reference_bytes = socket.send("set_spa_far_field_reff", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial ROI far Field Reference is ",5, return_value[])
#         time.sleep(5)
#         get_spa_far_field_reference(spa_far_field_reference_bytes[-8:])
#     def get_spa_far_field_reference(self,get_value_bytes):
#         get_x_value_bytes = get_value_bytes[0:4]
#         get_y_value_bytes = get_value_bytes[4:]
#         spa_far_field_reference_x_return_val =struct.unpack("<f",get_x_value_bytes)
#         spa_far_field_reference_y_return_val =struct.unpack("<f",get_y_value_bytes)
#         return spa_far_field_reference_x_return_val,spa_far_field_reference_y_return_val

#     def set_spa_near_field_reference(self, set_x_value, set_y_value):
#         set_x_value_bytes = struct.pack("<f", set_x_value)
#         set_y_value_bytes = struct.pack("<f", set_y_value)
#         set_value = set_x_value_bytes + set_y_value_bytes  
#         spa_near_field_reference_bytes = socket.send("set_spa_near_field_reff", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial ROI near Field Reference is ",5, return_value[])
#         time.sleep(5)
#         get_spa_near_field_reference(spa_near_field_reference_bytes[-8:])
#     def get_spa_near_field_reference(self,get_value_bytes):
#         get_x_value_bytes = get_value_bytes[0:4]
#         get_y_value_bytes = get_value_bytes[4:]
#         spa_near_field_reference_x_return_val =struct.unpack("<f",get_x_value_bytes)
#         spa_near_field_reference_y_return_val =struct.unpack("<f",get_y_value_bytes)
#         return spa_near_field_reference_x_return_val,spa_near_field_reference_y_return_val

#     def set_spa_gauss_order(self, set_value):
#         set_value = struct.pack("<d", set_value)
#         spa_gauss_order_bytes = socket.send("set_spa_gauss_order", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial Gauss Order is ",5, return_value[])
#         time.sleep(5)
#         get_spa_gauss_order(spa_near_field_reference_bytes[-8:])
#     def get_spa_gauss_order(self,get_value_bytes):
#         spa_gauss_order_return_val = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#         return spa_gauss_order_return_val
        
#     def set_spa_HWB(self, set_value):
#         set_value = struct.pack("<d", set_value)
#         spa_HWB_bytes = socket.send("set_spa_HWB", set_value_bytes)
#         return_value = socket.revieve(100)
#         print("wait time to set Spatial HWB is ",5, return_value[])
#         time.sleep(5)
#         get_spa_HWB(spa_HWB_bytes[-8:])
#     def get_spa_HWB(self,get_value_bytes):
#         spa_HWB_return_val = int.from_bytes(get_value_bytes, byteorder="little", signed=False)
#         return spa_HWB_return_val

        
#     def get_image_data(self):
#         str1 = _command_dict["get_image"]
#         socket.send(str1)
#         #size of the data that will be returned is 2457606, so the recv parameter size is set to 3000000
#         image_data = socket.recv(3000000)
#         time.sleep(config.long_wait)
#         return_value = socket.revieve(100)
#         print("wait time to Get Image:", config.long_wait)
#         image_data_output = image_data[6:]
#         length_of_image_data_1D = len(image_data_output)
#         return length_of_image_data_1D

#     def get_histogram_data(self):
#         str1 = _command_dict["get_histogram"]
#         socket.send(str1)
#         #size of the data that will be returned is 4102, so the recv parameter size is set to 5000
#         histogram_data = socket.recv(5000)
#         time.sleep(config.long_wait)
#         return_value = socket.revieve(100)
#         print("wait time to Get Histogram Data:", config.long_wait)
#         histogram_data_output = histogram_data[6:] #
#         length_of_histogram_data_1D = len(histogram_data_output)
#         return length_of_histogram_data_1D