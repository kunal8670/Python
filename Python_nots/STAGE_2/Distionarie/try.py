# Creating a dictionary

person = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}

#print(person["name"])  # Alice


#print(person["age"])       # 30
#print(person.get("name"))  # Alice
#print(person.get("height", "Not found"))  # Custom default

# person = {"name": "Kunal", "age": 22}
# for key in person:
#     print(key, person[key])  # name Kunal, age 22

# for k, v in person.items():
#     print(f"{k} → {v}")


sentence = "python is fun and python is powerful"
freq = {}

# for word in sentence.split():
#     freq[word] = freq.get(word, 0) 
#     print(word)
#     print(freq.get(word))

# print(freq)  # {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}

students = {
    "S001": {"name": "Kunal", "marks": 88},
    "S002": {"name": "Priya", "marks": 92},
}

#print(students["S001"]["marks"])  # 88



students = [
    ("Kunal", "A"), ("Ravi", "B"), ("Priya", "A"), ("Sneha", "C")
]

# grade_dict = {}
# for name, grade in students:
#     grade_dict.setdefault(grade, []).append(name)

# print(grade_dict)
# # {'A': ['Kunal', 'Priya'], 'B': ['Ravi'], 'C': ['Sneha']}


