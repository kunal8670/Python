#🔐 Challenge 2: Login Attempts Tracker – Using Tuples as Dictionary Keys
#💼 Scenario:
#You're designing a system to track failed login attempts.
#Each user login is tracked by:

#IP address

#Username

#But instead of storing data in separate keys, you want to use a tuple 
#(ip, username) as the key in a dictionary, and the value will be the 
#number of failed attempts.
#task:

#✅ 1. Count how many times each (ip, username) pair failed
#✅ 2. Store the result in a dictionary
#✅ 3. Print IP & Username if they have more than 2 failed attempts
#o/p
#('192.168.1.1', 'kunal') failed 3 times
#('10.0.0.5', 'admin') failed 2 times
#('10.0.0.9', 'guest') failed 1 times
#Too many attempts for: 192.168.1.1 - kunal


login_attempts = [
    ("192.168.1.1", "kunal"),
    ("10.0.0.5", "admin"),
    ("192.168.1.1", "kunal"),
    ("192.168.1.1", "kunal"),
    ("10.0.0.5", "admin"),
    ("10.0.0.9", "guest")
]

already_inlist=[]
max=0 #tmp for couting max

for i in login_attempts:
    
    if i not in already_inlist:
        t=login_attempts.count(i)
        print(f"{i} failed {t} times")

        already_inlist.append(i) # i want to add the sub tuple in list but....

        if t>max:   #for fetch max count
            max=t
            maxusr=f"{i[0]} - {i[1]}"

#print(f"{i} failed {t} times")
print(f"To many attemts for: {maxusr}")



