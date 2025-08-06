person = ("Kunal", 21, "India")
name, age, country = person
print(person)
name="harshad",55,"pakstan"

person=name, age, country 
print(person) 



# real use:
for index, value in enumerate(["a", "b"]):
    print(index, value)  # (index, value) → tuple unpacked
