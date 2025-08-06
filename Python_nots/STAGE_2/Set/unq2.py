#: Get all locations from sensor_logs where is_critical is True — but only show each location once.

sensor_logs = [
    ("S-101", "ServerRoom-1", 48.5, True),
    ("S-102", "ServerRoom-2", 35.0, False),
    ("S-101", "ServerRoom-1", 49.0, True),
    ("S-103", "ServerRoom-3", 32.0, False)
]

# Your task: Get {'S-101', 'S-102', 'S-103'}
unq=set()
for i,j,k,l in sensor_logs:
    if l==True:
        unq.add(j)

print(unq)
