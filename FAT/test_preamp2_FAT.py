# import pytest
# from lastronics_laser_amplifier_preamp2 import *
# from macros import *
# import time
# import struct
# import config
# from hamcrest import *


# @pytest.fixture(scope="module")
# def preamp2():
#     preamp2 = LastronicsLaserAmplifierPreAmp2(config.device_ip, config.device_port) #initialize the class + opens the connection
#     preamp2.set_connect_ldd()
#     preamp2.set_connect_pump_module()
#     preamp2.set_connect_amplifier()
#     preamp2.set_connect_chiller()
#     preamp2.set_connect_interlock()
#     yield preamp2
#     preamp2.close_connection()


# ### Test LDD Related Commands

# def test_WHEN_ldd_control_ON_command_is_set_THEN_ldd_control_mode_is_OPERATIONAL(preamp2):
#     #start by making device in standby mode
#     preamp2.set_ldd_ctrl(OFF)
#     preamp2.set_ldd_ctrl(ON)
#     assert preamp2.ldd_ctrl_mode == OPERATIONAL

# def test_WHEN_ldd_control_OFF_command_is_set_THEN_ldd_control_mode_is_STANDBY(preamp2):
#     preamp2.set_ldd_ctrl(OFF)
#     assert preamp2.ldd_ctrl_mode == STANDBY

# def test_GIVEN_ldd_control_is_ON_WHEN_lld_trigger_command_is_set_ON_THEN_trigger_status_is_ON(preamp2):
#     preamp2.set_ldd_ctrl(ON)#prerequisite for trigger
#     preamp2.set_ldd_trig(ON)
#     assert preamp2.trigger_status == TurnedOn

# def test_GIVEN_ldd_control_is_ON_WHEN_lld_trigger_command_is_set_OFF_THEN_trigger_status_is_OFF(preamp2):
#     #previous test should have set ldd control on
#     # preamp2.set_ldd_ctrl(ON)#prerequisite for trigger
#     preamp2.set_ldd_trig(OFF)
#     assert preamp2.trigger_status == TurnedOff

# def test_GIVEN_ldd_control_is_OFF_WHEN_lld_trigger_command_is_set_ON_THEN_trigger_status_is_OFF(preamp2):
#     preamp2.set_ldd_ctrl(OFF)#prerequisite for trigger
#     assert preamp2.ldd_ctrl_mode == STANDBY
#     #previous test should have set ldd trigger off
#     preamp2.set_ldd_trig(ON)
#     assert preamp2.trigger_status == TurnedOff

# def test_GIVEN_ldd_control_and_trigger_is_ON_WHEN_lld_channel_command_is_set_ON_THEN_channel_status_is_ON(preamp2):
#     preamp2.set_ldd_ctrl(ON)#prerequisite for trigger
#     preamp2.set_ldd_trig(ON)#prerequisite for channel
#     preamp2.set_ldd_chan(ON)
#     assert preamp2.channel_status == TurnedOn

# def test_GIVEN_ldd_control_and_trigger_is_ON_WHEN_lld_channel_command_is_set_OFF_THEN_channel_status_is_OFF(preamp2):
#     # previous test should have set ldd control, trigger and channel  on
#     # preamp2.set_ldd_ctrl(ON)#prerequisite for trigger
#     # preamp2.set_ldd_trig(ON)#prerequisite for channel
#     preamp2.set_ldd_chan(OFF)
#     assert preamp2.channel_status == TurnedOff

# def test_GIVEN_ldd_trigger_is_OFF_WHEN_lld_channel_command_is_set_ON_THEN_channel_status_is_not_ON(preamp2):
#     # previous test should have set ldd control on  and channel off
#     # preamp2.set_ldd_ctrl(ON)#prerequisite for trigger
#     preamp2.set_ldd_trig(OFF)#prerequisite for channel
#     assert preamp2.trigger_status == TurnedOff
#     preamp2.set_ldd_chan(ON)
#     assert preamp2.channel_status == TurnedOff


# @pytest.mark.parametrize(
#     "setting, expected", config.driver_pulse_current_set_value_when_pre_on
# )
# def test_GIVEN_ldd_prerequsites_are_ON_WHEN_lld_pulse_current_command_is_set_THEN_pulse_current_is_set_close_to_setting(preamp2, setting, expected):
#     preamp2.PreRequsites_to_set_ldd_parameters_ON()
#     preamp2.set_ldd_pulse_current(setting)
#     assert_that (preamp2.pulse_current_int, is_(close_to(expected, config.driver_pulse_current_tolerance)))

# @pytest.mark.parametrize(
#     "setting, expected", config.driver_pulse_current_set_value_when_pre_off
# )
# def test_GIVEN_ldd_prerequsites_are_OFF_WHEN_lld_pulse_current_command_is_set_THEN_pulse_current_is_NOT_set_to_setting(preamp2, setting, expected):
#     preamp2.PreRequsites_to_set_ldd_parameters_OFF()
#     preamp2.set_ldd_pulse_current(setting)
#     assert_that (preamp2.pulse_current_int, is_not(close_to(expected, config.driver_pulse_current_tolerance))) # supposed to fail

# @pytest.mark.parametrize(
#     "setting, expected", config.driver_bias_current_set_value_when_pre_on
# )
# def test_GIVEN_ldd_prerequsites_are_ON_WHEN_lld_bias_current_command_is_set_THEN_bias_current_is_set_close_to_setting(preamp2, setting, expected):
#     preamp2.PreRequsites_to_set_ldd_parameters_ON()
#     preamp2.set_ldd_bias_current(setting)
#     assert_that(preamp2.bias_current_float, is_(close_to(expected,config.driver_bias_current_tolerance)))

# @pytest.mark.parametrize(
#     "setting, expected", config.driver_bias_current_set_value_when_pre_off
# )
# def test_GIVEN_ldd_prerequsites_are_OFF_WHEN_lld_bias_current_command_is_set_THEN_bias_current_is_NOT_set_to_setting(preamp2, setting, expected):
#     preamp2.PreRequsites_to_set_ldd_parameters_OFF()
#     preamp2.set_ldd_bias_current(setting)
#     assert_that(preamp2.bias_current_float, is_not(close_to(expected,config.driver_bias_current_tolerance)))

# @pytest.mark.parametrize(
#     "setting, expected", config.driver_frequency_set_value_when_pre_on
# )
# def test_GIVEN_ldd_prerequsites_are_ON_WHEN_lld_frequency_command_is_set_THEN_frequency_is_set_close_to_setting(preamp2, setting, expected):
#     preamp2.PreRequsites_to_set_ldd_parameters_ON()
#     preamp2.set_ldd_freq(setting)
#     assert_that(preamp2.frequency_float, is_(close_to(expected,config.driver_frequency_tolerance)))

# @pytest.mark.parametrize(
#     "setting, expected", config.driver_frequency_set_value_when_pre_off
# )
# def test_GIVEN_ldd_prerequsites_are_OFF_WHEN_lld_frequency_command_is_set_THEN_frequency_is_NOT_set_to_setting(preamp2, setting, expected):
#     preamp2.PreRequsites_to_set_ldd_parameters_OFF()
#     preamp2.set_ldd_freq(setting)
#     assert_that(preamp2.frequency_float, is_not(close_to(expected,config.driver_frequency_tolerance)))

# @pytest.mark.parametrize(
#     "setting, expected", config.driver_pulse_width_set_value_when_pre_on
# )
# def test_GIVEN_ldd_prerequsites_are_ON_WHEN_lld_pulse_width_command_is_set_THEN_pulse_width_is_set_close_to_setting(preamp2, setting, expected):
#     preamp2.PreRequsites_to_set_ldd_parameters_ON()
#     preamp2.set_ldd_pulse_width(setting)
#     assert_that(preamp2.pulse_width_int, is_(close_to(expected, config.driver_pulse_current_tolerance)))

# @pytest.mark.parametrize(
#     "setting, expected", config.driver_pulse_width_set_value_when_pre_off
# )
# def test_GIVEN_ldd_prerequsites_are_OFF_WHEN_lld_pulse_width_command_is_set_THEN_pulse_width_is_NOT_set_to_setting(preamp2, setting, expected):
#     preamp2.PreRequsites_to_set_ldd_parameters_OFF()
#     preamp2.set_ldd_pulse_width(setting)
#     assert_that(preamp2.pulse_width_int, is_not(close_to(expected, config.driver_pulse_width_tolerance)))

# def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_mode_command_is_set_to_SINGLE_THEN_trigger_mode_is_SINGLE(preamp2):
#     preamp2.PreRequsites_to_set_ldd_parameters_ON()
#     preamp2.set_ldd_trigger_Continuous_single(Single)
#     assert preamp2.trigger_mode == single

# def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_mode_command_is_set_to_CONTINUOUS_THEN_trigger_mode_is_CONTINUOUS(preamp2):
#     preamp2.PreRequsites_to_set_ldd_parameters_ON()
#     preamp2.set_ldd_trigger_Continuous_single(Continuous)
#     assert preamp2.trigger_mode == Continuous

# def test_GIVEN_ldd_trigger_is_OFF_WHEN_lld_trigger_mode_command_is_set_to_SINGLE_THEN_trigger_mode_is_NOT_SINGLE(preamp2):
#     preamp2.PreRequsites_to_set_ldd_parameters_OFF()
#     # previous test should KEEP THE TRIGGER MODE TO CONTINUES
#     preamp2.set_ldd_trigger_Continuous_single(Single)
#     assert preamp2.trigger_mode != single

# def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_edge_command_is_set_to_POSITIVE_EDGE_THEN_trigger_edge_is_POSITIVE(preamp2):
#     preamp2.PreRequsites_to_set_ldd_parameters_ON()
#     preamp2.set_ldd_trigger_positive_negative(Positive)
#     assert preamp2.trigger_edge == positive

# def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_edge_command_is_set_to_NEGATIVE_EDGE_THEN_trigger_edge_is_NEGATIVE(preamp2):
#     preamp2.PreRequsites_to_set_ldd_parameters_ON()
#     preamp2.set_ldd_trigger_positive_negative(Negative)
#     assert preamp2.trigger_edge == negative

# def test_GIVEN_ldd_trigger_is_OFF_WHEN_lld_trigger_edge_command_is_set_to_POSITIVE_EDGE_THEN_trigger_edge_is_NOT_POSITIVE(preamp2):
#     preamp2.PreRequsites_to_set_ldd_parameters_OFF()
#     # PREVIOUS TEST SHOULD KEEP THE TRIGGER EDGE TO NEGATIVE
#     preamp2.set_ldd_trigger_positive_negative(Positive)
#     assert preamp2.trigger_edge != positive

# def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_source_command_is_set_to_EXTERNAL_THEN_trigger_source_is_EXTERNAL(preamp2):
#     preamp2.PreRequsites_to_set_ldd_parameters_ON()
#     preamp2.set_ldd_trigger_internal_external(External)
#     assert preamp2.trigger_source == external

# def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_source_command_is_set_to_INTERNAL_THEN_trigger_source_is_INTERNAL(preamp2):
#     preamp2.PreRequsites_to_set_ldd_parameters_ON()
#     preamp2.set_ldd_trigger_internal_external(Internal)
#     assert preamp2.trigger_source == internal

# def test_GIVEN_ldd_trigger_is_ON_WHEN_lld_trigger_source_command_is_set_to_EXTERNAL_THEN_trigger_source_is_NOT_EXTERNAL(preamp2):
#     preamp2.PreRequsites_to_set_ldd_parameters_OFF()
#     # PREVIOUS TEST SHOULD KEEP TRIGGER SOURCE TO INTERNAL
#     preamp2.set_ldd_trigger_internal_external(External)
#     assert preamp2.trigger_source != external

# def test_WHEN_ldd_soft_start_is_set_to_ON_THEN_check_ldd_soft_start_status_is_ENABLED(preamp2):
#     preamp2.set_ldd_softstart(ON)
#     assert preamp2.softstart_status == Soft_Start_Enabled

# def test_WHEN_ldd_soft_start_is_set_to_OFF_THEN_check_ldd_soft_start_status_is_DISABLED(preamp2):
#     preamp2.set_ldd_softstart(OFF)
#     assert preamp2.softstart_status == Soft_Start_Disabled

# ## Water Chiller

# def test_WHEN_water_chiller_ON_command_is_set_THEN_chiller_status_is_OPERATIONAL(preamp2):
#     preamp2.set_water_chiller_control(ON)
#     assert preamp2.water_chiller_operational_status == OPERATIONAL

# def test_WHEN_water_chiller_OFF_command_is_set_THEN_chiller_status_is_STANDBY(preamp2):
#     preamp2.set_water_chiller_control(OFF)
#     assert preamp2.water_chiller_operational_status == STANDBY

# @pytest.mark.parametrize(
#     "setting, expected", config.chiller_setpoint_temperature_set_value
# )
# def test_GIVEN_chiller_is_operational_WHEN_water_chiller_temperature_is_set_THEN_check_the_temperature_is_set(preamp2, setting, expected):
#     preamp2.set_water_chiller_control(ON)
#     preamp2.set_water_chiller_temperature_setpoint(18.0)
#     preamp2.set_water_chiller_temperature_setpoint(setting)
#     assert_that(preamp2.water_chil_setpoint_temp_float, is_(close_to(expected, config.chiller_setpoint_temperature_tolerance)))

# @pytest.mark.parametrize(
#     "setting, expected", config.chiller_setpoint_temperature_set_value
# )
# def test_GIVEN_chiller_is_standby_WHEN_water_chiller_temperature_is_set_THEN_check_the_temperature_is_set(preamp2, setting, expected):
#     preamp2.set_water_chiller_control(OFF)
#     preamp2.set_water_chiller_temperature_setpoint(setting)
#     assert_that(preamp2.water_chil_setpoint_temp_float, is_(close_to(expected, config.chiller_setpoint_temperature_tolerance)))

# def test_WATER_CHILLER_WATER_FLOW_RATE_is_within_limits(preamp2):
#     preamp2.get_water_chil_water_flow_rate()
#     assert_that(preamp2.water_chill_water_flow_rate_float, is_(greater_than_or_equal_to(config.water_chill_water_flow_rate_min_allowable_value)))
#     assert_that(preamp2.water_chill_water_flow_rate_float, is_(less_than_or_equal_to(config.water_chill_water_flow_rate_max_allowable_value)))

# def test_WATER_CHILLER_WATER_TEMPERATURE_is_within_limits(preamp2):
#     preamp2.get_water_chil_water_temperature()
#     assert_that(preamp2.water_chill_water_temperature_float, is_(greater_than_or_equal_to(config.water_chill_water_temperature_min_allowable_value)))
#     assert_that(preamp2.water_chill_water_temperature_float, is_(less_than_or_equal_to(config.water_chill_water_temperature_max_allowable_value)))


# ### Amplifier Commands

# def test_WHEN_amplifier_control_is_set_to_OFF_THEN_check_amplifier_operational_status_is_STANDBY(preamp2):
#     preamp2.set_amplifier_control(OFF)
#     assert preamp2.amplifier_operation_status == STANDBY

# def test_WHEN_amplifier_control_is_set_to_ON_THEN_check_amplifier_operational_status_is_OPERATIONAL(preamp2):
#     preamp2.set_amplifier_control(ON)
#     assert preamp2.amplifier_operation_status == OPERATIONAL

# @pytest.mark.parametrize(
#     "setting, expected", config.amplifier_target_temperature_set_value_when_ctrl_on
# )
# def test_GIVEN_amplifier_control_is_operational_WHEN_amplifier_temperature_is_set_THEN_check_the_laser_material_temperature_is_set_close_to_setting(preamp2, setting, expected):
#     # preamp2.set_amplifier_control(ON)
#     preamp2.set_amplifier_target_temperature(setting)
#     assert_that(preamp2.amplifier_target_temp_float, is_(close_to(expected, config.amplifier_target_temperature_tolerance)))

# @pytest.mark.parametrize(
#     "setting, expected", config.set_amplifier_target_temperature
# )
# def test_GIVEN_amplifier_control_is_standby_WHEN_amplifier_temperature_is_set_THEN_check_the_laser_material_temperature_is_set_close_to_setting(preamp2, setting, expected):
#     # preamp2.set_amplifier_control(OFF)
#     preamp2.set_amplifier_target_temperature(setting)
#     assert_that(preamp2.amplifier_target_temp_float, is_(close_to(expected, config.amplifier_target_temperature_tolerance)))

# def test_amplifier_base_plate_temperature_is_within_range(preamp2):
#     assert_that(preamp2.get_amplifier_base_plate_temperature(),is_(greater_than_or_equal_to(config.amplifier_base_plate_temperature_expected_min_allowable_value)))
#     assert_that(preamp2.get_amplifier_base_plate_temperature(),is_(less_than_or_equal_to(config.amplifier_base_plate_temperature_expected_max_allowable_value)))

# def test_amplifier_laser_material_temperature_is_within_range(preamp2):
#     assert_that(preamp2.get_amplifier_laser_material_temperature(),is_(greater_than_or_equal_to(config.amplifier_laser_material_temperature_expected_min_allowable_value)))
#     assert_that(preamp2.get_amplifier_laser_material_temperature(),is_(less_than_or_equal_to(config.amplifier_laser_material_temperature_expected_max_allowable_value)))

# def test_amplifier_vacuum_pressure_is_within_range(preamp2):
#     assert_that(preamp2.get_amplifier_vacuum_pressure_float(),is_(greater_than_or_equal_to(config.amplifier_vacuum_pressure_expected_min_allowable_value)))
#     assert_that(preamp2.get_amplifier_vacuum_pressure_float(),is_(less_than_or_equal_to(config.amplifier_vacuum_pressure_expected_max_allowable_value)))

    

# ### Test SPA Diagnoistics commands

# # @pytest.mark.parametrize(
# #     "setting, expected", config.spa_divider_set_value
# # )
# # def test_WHEN_spa_spatial_divider_is_set_to_setting_THEN_check_spatial_divider_is_expected(preamp2, setting, expected):
# #     preamp2.set_spatial_divider(setting)
# #     assert_that(preamp2.spa_divider, is_(expected))

# # @pytest.mark.parametrize(
# #     "setting, expected", config.spa_gain_raw_set_value
# # )
# # def test_WHEN_spa_spatial_gain_is_set_to_setting_THEN_check_spatial_gain_is_expected(preamp2, setting, expected):
# #     preamp2.set_spatial_gain(setting)
# #     assert_that(preamp2.spa_gain, is_(expected))
    
# # @pytest.mark.parametrize(
# #     "setting, expected", config.spa_black_level_set_value
# # )
# # def test_WHEN_spa_spatial_black_level_is_set_to_setting_THEN_check_spatial_black_level_is_expected(preamp2, setting, expected):
# #     preamp2.set_spatial_black_level_gain(setting)
# #     assert_that(preamp2.spa_black_level_gain, is_(expected))

# # def test_WHEN_spa_spatial_trigger_mode_is_set_to_0_THEN_check_spatial_trigger_mode_is_turned_OFF(preamp2):
# #     preamp2.set_spatial_trigger_mode(0)
# #     assert preamp2.spa_trigger_mode == Trigger_Off 

# # def test_WHEN_spa_spatial_trigger_mode_is_set_to_1_THEN_check_spatial_trigger_mode_is_turned_ON(preamp2):
# #     preamp2.set_spatial_trigger_mode(1)
# #     assert preamp2.spa_trigger_mode == Trigger_On

# # def test_WHEN_spa_spatial_trigger_source_is_set_to_0_THEN_check_spatial_trigger_source_is_in_SOFTWARE(preamp2):
# #     preamp2.set_spatial_trigger_source(0)
# #     assert preamp2.spa_trigger_source == Software 

# # def test_WHEN_spa_spatial_trigger_source_is_set_to_line_1_THEN_check_spatial_trigger_source_is_in_LINE_1(preamp2):
# #     preamp2.set_spatial_trigger_source(line1)
# #     assert preamp2.spa_trigger_source == line_1

# # def test_WHEN_spa_spatial_trigger_source_is_set_to_line_2_THEN_check_spatial_trigger_source_is_in_LINE_2(preamp2):
# #     preamp2.set_spatial_trigger_source(line2)
# #     assert preamp2.spa_trigger_source == line_2

# # def test_WHEN_spatial_trigger_edge_command_is_set_to_ON_THEN_spatial_trigger_edge_is_POSITIVE_edge(preamp2):
# #     preamp2.set_spatial_trigger_edge(ON)
# #     assert preamp2.spa_trigger_edge == Positive 

# # def test_WHEN_spatial_trigger_edge_command_is_set_to_OFF_THEN_spatial_trigger_edge_is_NEGATIVE_edge(preamp2):
# #     preamp2.set_spatial_trigger_edge(OFF)
# #     assert preamp2.spa_trigger_edge == Negative

# # @pytest.mark.parametrize(
# #     "setting, expected", config.spa_trigger_delay_absloute_set_value
# # )
# # def test_WHEN_spatial_trigger_delay_absolute_command_is_set_to_setting_value_THEN_spatial_trigger_delay_absolute_is_expected(preamp2, setting, expected):
# #     preamp2.set_spatial_trigger_delay_absloute(setting)
# #     assert_that(preamp2.spa_trigger_delay_absloute, is_(expected)) 
    
# # @pytest.mark.parametrize(
# #     "setting, expected", config.spa_exposure_time_absloute_set_value
# # )
# # def test_WHEN_spatial_exposure_time_absolute_command_is_set_to_setting_value_THEN_spatial_exposure_time_absolute_is_expected(preamp2, setting, expected):
# #     preamp2.set_spatial_exposure_time_absloute(setting)
# #     assert_that(preamp2.spa_exposure_time_absloute, is_(expected)) 

# # def test_WHEN_spatial_save_background_command_is_set_to_ON_THEN_spatial_save_background_is_save(preamp2):
# #     preamp2.set_spa_save_background(ON)
# #     assert preamp2.spa_save_background_return_val == Save

# # def test_WHEN_spatial_save_background_command_is_set_to_OFF_THEN_spatial_save_background_is_OFF(preamp2):
# #     preamp2.set_spa_save_background(OFF)
# #     assert preamp2.spa_save_background_return_val == IsOff

# # def test_WHEN_spatial_substract_background_command_is_set_to_ON_THEN_spatial_substract_background_is_substract(preamp2):
# #     preamp2.set_spa_substract_background(ON)
# #     assert preamp2.spa_substract_background_return_val == Substract

# # def test_WHEN_spatial_substract_background_command_is_set_to_OFF_THEN_spatial_substract_background_is_off(preamp2):
# #     preamp2.set_spa_substract_background(OFF)
# #     assert preamp2.spa_substract_background_return_val == IsOff

# # @pytest.mark.parametrize(
# #     "setting, expected", config.spa_n_background_averages_set_value
# # )
# # def test_WHEN_spatial_N_background_averages_command_is_set_to_setting_THEN_spatial_n_background_averages_is_as_expected(preamp2, setting, expected):
# #     preamp2.set_spa_N_background_averages(setting)
# #     assert preamp2.spa_n_backgnd_avgs_return_val == expected

# # @pytest.mark.parametrize(
# #     "setting, expected", config.spa_number_of_ticks_in_legend_set_value
# # )
# # def test_WHEN_spatial_number_of_ticks_in_legend_command_is_set_to_setting_THEN_spatial_number_of_ticks_in_legend_is_as_expected(preamp2, setting, expected):
# #     preamp2.set_spa_number_of_ticks_in_ledgend(setting)
# #     assert preamp2.spa_number_of_ticks_in_ledgend_return_val == expected


# # def test_WHEN_spatial_adjustments_mode_command_is_set_to_ON_THEN_spatial_adjustments_mode_is_ON(preamp2):
# #     preamp2.set_spa_adjustments_mode(ON)
# #     assert preamp2.spa_adjustments_mode_return_val == IsOn

# # def test_WHEN_spatial_adjustments_mode_command_is_set_to_OFF_THEN_spatial_adjustments_mode_is_OFF(preamp2):
# #     preamp2.set_spa_adjustments_mode(OFF)
# #     assert preamp2.spa_adjustments_mode_return_val == IsOff


# # @pytest.mark.parametrize(
# #     "setting, expected", config.spa_image_averages_set_value
# # )
# # def test_WHEN_spatial_image_averages_command_is_set_to_setting_THEN_spatial_image_averages_is_as_expected(preamp2, setting, expected):
# #     preamp2.set_spa_image_averages(setting)
# #     assert preamp2.spa_image_average_return_val == expected

# # def test_spatial_n_pictures_in_stack_is_as_expected(preamp2):
# #     preamp2.get_spa_N_pictures_in_stack()
# #     assert preamp2.spa_n_backgnd_avgs_return_val == expected

# # def test_WHEN_spatial_camera_standard_properties_command_is_set_to_ON_THEN_spatial_camera_standard_properties_is_ON(preamp2):
# #     preamp2.set_spa_camera_standard_properties(ON)
# #     assert preamp2.spa_cam_standard_properties_return_val == IsOn

# # def test_WHEN_spatial_camera_standard_properties_command_is_set_to_OFF_THEN_spatial_camera_standard_properties_is_OFF(preamp2):
# #     preamp2.set_spa_camera_standard_properties(OFF)
# #     assert preamp2.spa_cam_standard_properties_return_val == IsOff


# # @pytest.mark.parametrize(
# #     "expected_X_VALUE, expected_Y_VALUE", config.spa_far_field_XY_centroid_expected
# # )
# # def test_spatial_far_field_XY_centroid_is_as_expected(preamp2, expected_X_VALUE, expected_Y_VALUE):
# #     preamp2.get_spa_far_field_XY_centroid()
# #     assert_that(preamp2.spa_far_field_X_centroid_return_value, is_(close_to(expected_X_VALUE, config.spa_far_field_X_centroid_tolerance)))
# #     assert_that(preamp2.spa_far_field_Y_centroid_return_value, is_(close_to(expected_Y_VALUE, config.spa_far_field_Y_centroid_tolerance)))

# # @pytest.mark.parametrize(
# #     "expected_X_VALUE, expected_Y_VALUE", config.spa_near_field_XY_centroid_expected
# # )
# # def test_spatial_near_field_XY_centroid_is_as_expected(preamp2, expected_X_VALUE, expected_Y_VALUE):
# #     preamp2.get_spa_near_field_XY_centroid()
# #     assert_that(preamp2.spa_near_field_X_centroid_return_value, is_(close_to(expected_X_VALUE, config.spa_near_field_X_centroid_tolerance)))
# #     assert_that(preamp2.spa_near_field_Y_centroid_return_value, is_(close_to(expected_Y_VALUE, config.spa_near_field_Y_centroid_tolerance)))

# # @pytest.mark.parametrize(
# #     "expected_X_VALUE, expected_Y_VALUE", config.spa_far_field_delta_XY_centroid_expected
# # )
# # def test_spatial_far_field_delta_XY_centroid_is_as_expected(preamp2, expected_X_VALUE, expected_Y_VALUE):
# #     preamp2.get_spa_far_field_DELTA_XY_centroid()
# #     assert_that(preamp2.spa_far_field_delta_X_centroid_return_value, is_(close_to(expected_X_VALUE, config.spa_far_field_delta_X_centroid_tolerance)))
# #     assert_that(preamp2.spa_far_field_delta_Y_centroid_return_value, is_(close_to(expected_Y_VALUE, config.spa_far_field_delta_Y_centroid_tolerance)))

# # @pytest.mark.parametrize(
# #     "expected_X_VALUE, expected_Y_VALUE", config.spa_near_field_delta_XY_centroid_expected
# # )
# # def test_spatial_near_field_delta_XY_centroid_is_as_expected(preamp2, expected_X_VALUE, expected_Y_VALUE):
# #     preamp2.get_spa_NEAR_field_DELTA_XY_centroid()
# #     assert_that(preamp2.spa_near_field_delta_X_centroid_return_value, is_(close_to(expected_X_VALUE, config.spa_near_field_delta_X_centroid_tolerance)))
# #     assert_that(preamp2.spa_near_field_delta_Y_centroid_return_value, is_(close_to(expected_Y_VALUE, config.spa_near_field_delta_Y_centroid_tolerance)))

# # @pytest.mark.parametrize(
# #     "expected", config.spa_energy_expected
# # )
# # def test_spatial_energy_is_as_expected(preamp2, expected):
# #     preamp2.get_spa_energy()
# #     assert_that(preamp2.spa_energy_return_value, is_(expected)) 

# # @pytest.mark.parametrize(
# #     "setting, expected", config.spa_energy_claibration_factor_set_value
# # )
# # def test_spatial_energy_calibration_factor_is_as_expected(preamp2, setting, expected):
# #     preamp2.set_spa_energy_calibration_factor(setting)
# #     assert preamp2.spa_energy_calibration_factor_return_val == expected

# # @pytest.mark.parametrize(
# #     "X_VALUE, Y_VALUE, RAD_VALUE, expected_X_VALUE, expected_Y_VALUE, expected_RAD_VALUE", config.spa_ROI_near_field_set_value
# # )
# # def test_WHEN_spatial_roi_near_field_command_is_set_to_setting_THEN_spatial_roi_near_field_X_Y_and_Rad_is_as_expected(preamp2, X_VALUE, Y_VALUE, RAD_VALUE, expected_X_VALUE, expected_Y_VALUE, expected_RAD_VALUE):
# #     preamp2.set_spa_ROI_near_field(X_VALUE,Y_VALUE,RAD_VALUE)
# #     assert preamp2.spa_ROI_near_field_x_return_val == expected_X_VALUE
# #     assert preamp2.spa_ROI_near_field_y_return_val == expected_Y_VALUE
# #     assert preamp2.spa_ROI_near_field_rad_return_val == expected_RAD_VALUE

# # @pytest.mark.parametrize(
# #     "X_VALUE, Y_VALUE, RAD_VALUE, expected_X_VALUE, expected_Y_VALUE, expected_RAD_VALUE", config.spa_ROI_far_field_set_value
# # )
# # def test_WHEN_spatial_roi_far_field_command_is_set_to_setting_THEN_spatial_roi_far_field_X_Y_and_Rad_is_as_expected(preamp2, X_VALUE, Y_VALUE, RAD_VALUE, expected_X_VALUE, expected_Y_VALUE, expected_RAD_VALUE):
# #     preamp2.set_spa_ROI_far_field(X_VALUE,Y_VALUE,RAD_VALUE)
# #     assert preamp2.spa_ROI_far_field_x_return_val == expected_X_VALUE
# #     assert preamp2.spa_ROI_far_field_y_return_val == expected_Y_VALUE
# #     assert preamp2.spa_ROI_far_field_rad_return_val == expected_RAD_VALUE
    
# # @pytest.mark.parametrize(
# #     "X_VALUE, Y_VALUE, expected_X_VALUE, expected_Y_VALUE", config.spa_near_field_reference_set_value
# # )
# # def test_WHEN_spatial_near_field_reference_command_is_set_to_setting_THEN_spatial_near_field_reference_X_Y_is_as_expected(preamp2, X_VALUE, Y_VALUE, expected_X_VALUE, expected_Y_VALUE):
# #     preamp2.set_spa_near_field_reference(X_VALUE,Y_VALUE,RAD_VALUE)
# #     assert_that(preamp2.spa_near_field_reference_x_return_val, is_(expected_X_VALUE))
# #     assert_that(preamp2.spa_near_field_reference_y_return_val, is_(expected_Y_VALUE))

    
# # @pytest.mark.parametrize(
# #     "X_VALUE, Y_VALUE, expected_X_VALUE, expected_Y_VALUE", config.spa_far_field_reference_set_value
# # )
# # def test_WHEN_spatial_far_field_reference_command_is_set_to_setting_THEN_spatial_far_field_reference_X_Y_is_as_expected(preamp2, X_VALUE, Y_VALUE, expected_X_VALUE, expected_Y_VALUE):
# #     preamp2.set_spa_far_field_reference(X_VALUE,Y_VALUE,RAD_VALUE)
# #     assert_that(preamp2.spa_far_field_reference_x_return_val, is_(expected_X_VALUE))
# #     assert_that(preamp2.spa_far_field_reference_y_return_val, is_(expected_Y_VALUE))

# # @pytest.mark.parametrize(
# #     "setting, expected", config.spa_gauss_order_set_value
# # )
# # def test_WHEN_spatial_gauss_order_command_is_set_to_setting_THEN_spatial_gauss_order_is_as_expected(preamp2, setting, expected):
# #     preamp2.set_spa_gauss_order(setting)
# #     assert preamp2.spa_gauss_order_return_val == expected

# # @pytest.mark.parametrize(
# #     "setting, expected",config.spa_HWB_set_value
# # )
# # def test_WHEN_spatial_HWB_command_is_set_to_setting_THEN_spatial_HWB_is_as_expected(preamp2, setting, expected):
# #     preamp2.set_spa_HWB(setting)
# #     assert preamp2.spa_HWB_return_val == expected

# # def test_WHEN_spatial_image_is_get_THEN_image_received_size_is_correct(preamp2):
# #     preamp2.get_image_data()
# #     assert preamp2.length_of_image_data_1D == config.spa_defined_image_size

# # def test_WHEN_spatial_histogram_is_get_THEN_histogram_received_size_is_correct(preamp2):
# #     preamp2.get_histogram_data()
#     assert preamp2.length_of_histogram_data_1D == config.spa_defined_histogram_size

# ### Test Pump Module Get values

# def test_WHEN_not_chill_THEN_pump_module_temperature_is_within_room_temperature(preamp2):
#     assert_that(preamp2.get_pump_module_temperature_float(),is_(greater_than_or_equal_to(config.pump_module_temperature_min_allowable_value)))
#     assert_that(preamp2.get_pump_module_temperature_float(),is_(less_than_or_equal_to(config.pump_module_temperature_max_allowable_value)))
    
# def test_PUMP_MODULE_humidity_is_within_range(preamp2):
#     assert_that(preamp2.get_pump_module_humidity_float(),is_(greater_than_or_equal_to(config.pump_module_relative_humidity_min_allowable_value)))
#     assert_that(preamp2.get_pump_module_humidity_float(),is_(less_than_or_equal_to(config.pump_module_relative_humidity_max_allowable_value)))


# def test_PUMP_MODULE_water_flow_is_within_range(preamp2):
#     assert_that(preamp2.get_pump_module_water_flow_float(),is_(greater_than_or_equal_to(config.pump_module_water_flow_min_allowable_value)))
#     assert_that(preamp2.get_pump_module_water_flow_float(),is_(less_than_or_equal_to(config.pump_module_water_flow_max_allowable_value)))

# def test_PUMP_MODULE_counter_is_within_range(preamp2):
#     assert_that(preamp2.get_pump_module_pulse_counter_float(),is_(greater_than_or_equal_to(config.pump_module_pulse_count_min_allowable_value)))
#     assert_that(preamp2.get_pump_module_pulse_counter_float(),is_(less_than_or_equal_to(config.pump_module_pulse_count_max_allowable_value)))


# ### Test all the Errors are NOT ACTIVE

# def test_WHEN_device_is_operated_THEN_operational_parameters_are_OK(preamp2):
#     assert preamp2.get_internal_bus_err() == No_Error
#     assert preamp2.get_mosfet_temp_err() == No_Error
#     assert preamp2.get_capacitor_temp_err() == No_Error
#     assert preamp2.get_heatsink_temp_err() == No_Error
#     assert preamp2.get_interlock_err() == No_Error
#     assert preamp2.get_pulse_shape_err() == No_Error
#     assert preamp2.get_smps_power_err() == No_Error
#     assert preamp2.get_smps_temp_err() == No_Error
#     assert preamp2.get_capacitor_charge_err() == No_Error


# def test_WHEN_WATER_CHILLER_is_operated_THEN_operational_parameters_are_OK(preamp2):
#     assert preamp2.get_low_temp_error() == no_Error
#     assert preamp2.get_high_temp_error() == no_Error
#     assert preamp2.get_low_temp_warning() == no_Error
#     assert preamp2.get_high_temp_warning() == no_Error
#     assert preamp2.get_water_chil_water_flow_error() == no_Error
#     assert preamp2.get_low_pressure_error() == no_Error
#     assert preamp2.get_water_chil_water_level_error() == no_Error
#     assert preamp2.get_water_chil_dry_run_error() == no_Error
#     assert preamp2.get_high_pressure_error() == no_Error
#     assert preamp2.get_remote_control_error() == no_Error


# def test_PUMP_MODULE_parameters_are_OK(preamp2):
#     assert preamp2.get_pump_module_tcp_connection_error() == no_Error
#     assert preamp2.get_pump_module_leakage_error() == no_Error
#     assert preamp2.get_pump_module_forward_voltage_error() == no_Error
#     assert preamp2.get_pump_module_temperature_error() == no_Error
#     assert preamp2.get_pump_module_humidity_error() == no_Error
#     assert preamp2.get_pump_module_water_flow_error() == no_Error  


# def test_AMPLIFIER_parameters_are_OK(preamp2):
#     assert preamp2.get_amplifier_base_plate_temperature_error() == no_Error
#     assert preamp2.get_amplifier_laser_material_temperature_error() == no_Error
#     assert preamp2.get_amplifier_amplifier_vacuum_error() == no_Error
#     assert preamp2.get_amplifier_amplifier_tcp_connection_error() == no_Error


# def test_INTERLOCK_parameters_are_OK(preamp2):
#     preamp2.get_interlock_sta()
#     assert preamp2.interlock_pump_module_error == no_Error
#     assert preamp2.interlock_water_cooling_error == no_Error
#     assert preamp2.interlock_amp_ctrl_error == no_Error
#     assert preamp2.interlock_external_error == no_Error
#     assert preamp2.interlock_reset_required == no_Error
#     assert preamp2.interlock_tcp_connection_error == no_Error

