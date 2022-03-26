import json
import configparser
config = configparser.ConfigParser()

config.add_section('global')
config.set('global', 'timezone', '-8:00')
config.set('global', 'clock_type', '24h')
config.set('global', 'measurement_unit', 'imperial')
config.set('global', 'time_source', 'gps')

config.add_section('gps')
config.set('gps', 'installed', 'True')
config.set('gps', 'update_hz', '1')
config.set('gps', 'speed_alarm', '35')

config.add_section('turn_signal')
config.set('turn_signal', 'installed', 'True')
config.set('turn_signal', 'flash_hz', '1.0')
config.set('turn_signal', 'use_brake_light', 'False')

config.add_section('hazard_light')
config.set('hazard_light', 'installed', 'True')
config.set('hazard_light', 'flash_hz', '1.0')
config.set('hazard_light', 'use_brake_light', 'False')
config.set('hazard_light', 'use_turn_signal', 'True')

config.add_section('headlight')
config.set('headlight', 'installed', 'True')
config.set('headlight', 'strobe', 'False')
config.set('headlight', 'strobe_hz', '10')
config.set('headlight', 'high_beam', 'True')
config.set('headlight', 'fog_lights', 'False')

config.add_section('heated_seat')
config.set('heated_seat', 'installed', 'True')
config.set('heated_seat', 'pwr_levels', '1')

config.add_section('grip_heaters')
config.set('grip_heaters', 'installed', 'True')
config.set('grip_heaters', 'pwr_levels', '1')

config.add_section('stereo')
config.set('stereo', 'installed', 'True')
config.set('stereo', 'connection_type', 'bluetooth')
config.set('stereo', 'streaming_service', 'spotify')

config.add_section('horn')
config.set('horn', 'installed', 'True')
config.set('horn', 'save_vid_on_honk', 'True')

config.add_section('dash_cam')
config.set('dash_cam', 'installed', 'True')
config.set('dash_cam', 'storage_path', '~./dashcam/')
config.set('dash_cam', 'front_cam_installed', 'True')
config.set('dash_cam', 'rear_cam_installed', 'True')
config.set('dash_cam', 'front_cam_device', 'cam01')
config.set('dash_cam', 'rear_cam_device', 'cam02')

# Writing our configuration file to 'example.cfg'
#with open('example.cfg', 'wb') as configfile:

with open('example.cfg', 'w') as configfile:
    config.write(configfile)

print(config['gps']['installed'])

