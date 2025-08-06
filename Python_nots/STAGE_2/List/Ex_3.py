students = [["Alice", 85], ["Bob", 92], ["Charlie", 78]]

# Sort by score (second element)
students.sort(key=lambda x: x[1], reverse=True)

print("Sorted Students:")
for name, score in students:
    print(f"{name}: {score}")
