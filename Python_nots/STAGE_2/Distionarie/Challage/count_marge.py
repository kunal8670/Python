# 👉 Build a dictionary `count_fruits` like:
# {'apple': 3, 'banana': 2, 'cherry': 1}
# Then update it using `fruits2`
# Final output should show:
# {'apple': 3, 'banana': 4, 'cherry': 2, 'grape': 1}

# 🚀 Your task: Write full code for this logic


# Initial fruits
fruits1 = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Update list
fruits2 = ["banana", "cherry", "banana", "grape"]
count={}

for key in fruits1:
    print(key)
    count[key]=count.get(key,0)+1
print(count)   

fruits3=fruits1+fruits2
count.clear()
for key in fruits3:
    count[key]=count.get(key,0)+1
print(count)
