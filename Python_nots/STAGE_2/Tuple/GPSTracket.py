#✅ Tuple Challenge 1: GPS Tracker (Real-World + Basics)
#📌 Problem:
#You’re building a GPS tracker. Store the locations of users using 
#immutable structures. Create a structure to hold username and location
#(latitude, longitude). Then print all locations in readable form.

users = [
    ("Kunal", (18.5204, 73.8567)),
    ("Amit", (28.7041, 77.1025)),   
    ("Sara", (12.9716, 77.5946))
]

for i,(j,k) in users:
    print(f"{i} is at Latitude {j} and Longitude {k}")
  
#print(users[0]) #('Kunal', (18.5204, 73.8567))
#print(users[0][1]) #(18.5204, 73.8567)
#print(users[0][1][0]) #18.5204
