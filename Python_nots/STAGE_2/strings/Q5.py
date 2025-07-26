#Print only the Python files 

files = ["main.py", "app.js", "config.py", "style.css"]

for i in files:
    if i.endswith('.py'): #Twist: How endswith() worn in list:-
         print(i)         #endswith is method of string and elment of list are strings so its works
        
print([i for i in files if i.endswith('.py')])#one liner

#we can pass tupple inside endswith 
