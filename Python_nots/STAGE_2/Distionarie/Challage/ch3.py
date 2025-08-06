#Create a dictionary using .get() to count how many times each color appears.
#⛔ Don't use collections.Counter or count().
#✅ Use only .get().

colors = ["red", "blue", "red", "green", "blue", "blue"]

dst={}
for key in colors:
    dst[key]=dst.get(key,0)+1

print(dst)    

