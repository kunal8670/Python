sensor_logs = [
    ("S-101", "ServerRoom-1", 48.5, True),
    ("S-102", "ServerRoom-2", 35.0, False),
    ("S-101", "ServerRoom-1", 49.0, True),
    ("S-103", "ServerRoom-3", 32.0, False),
    ("S-101", "ServerRoom-1", 45.5, True),
    ("S-102", "ServerRoom-2", 42.0, True),
    ("S-103", "ServerRoom-3", 30.5, False)
]

#print(sensor_logs[0])
#print(sensor_logs[0][3])
#print([ is_critical for sensor_id, location, temperature, is_critical in sensor_logs if is_critical==True])
