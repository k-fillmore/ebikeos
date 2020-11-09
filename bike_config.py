import json

config = {}
config['GPS'] = []
config['GPS'].append({
    'installed': True,
    'update_hz': 1,
})
config['turn_signal'] = []
config['turn_signal'].append({
    'installed': True,
    'flash_interval': 1,
    'use_brake_light': False
})
config['hazard_lights'] = []
config['hazard_lights'].append({
    'installed': True,
    'flash_interval': 1,
    'use_turn_signal': True,
    'use_brake_light': False
})
config['grip_heaters'] = []
config['grip_heaters'].append({
    'installed': False,
    'num_levels': 1
})
config['global'] = []
config['global'].append({
    'timezone': '-8',
    'clock_type': '24h',
    'measurement_unit': 'imperial',
    'time_source': 'gps',

})