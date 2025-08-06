# 🧠 Python Lists – All Questions, Hints & Answers (with Comprehensions)

---

## Q1. Add multiple elements to a list  
**Hint:** Use `.extend()` to add more than one item at once  
**Answer:**  
```python
lst = []
lst.extend([1, "kunal", 2.3, 'P'])
```

---

## Q2. Remove a specific value and pop the last item  
**Hint:** `.remove()` deletes by value; `.pop()` removes last item  
**Answer:**
```python
data.remove("remove_me")
data.pop()
print(data)
```

---

## Q3. Count how many times "pen" appears and check if it's duplicate  
**Hint:** Use loop or `.count()`, then condition on count  
**Answer:**
```python
items = ["pen", "pencil", "eraser", "pen", "scale"]
tmp = 0
for i in items:
    if i == "pen":
        tmp += 1
print(f"Found {tmp} times")

if tmp > 1:
    print("Duplicate found")
else:
    print("Unique")
```

---

## Q4. Insert at a specific position, replace a value, and find index  
**Hint:** `.insert(pos, val)` adds at position, `list[index] = val` replaces, loop/index() to find  
**Answer:**
```python
users = ["admin", "guest", "john", "doe"]
users.insert(1, "new_user")
users[3] = "anonymous"
for i in range(len(users)):
    if users[i] == "admin":
        print(f"Index of admin: {i}")
```

---

## Q5. Count, remove, append, and sort  
**Hint:** `.count(val)`, `.remove(val)`, `.append(val)`, `.sort()`  
**Answer:**
```python
nums = [1, 4, 6, 4, 3, 4, 9]
print("Count of 4 is:", nums.count(4))
nums.remove(4)  # removes first occurrence
nums.append(100)
nums.sort()
print(nums)
```

---

## Q6. List comprehension – square numbers  
**Hint:** Use `[expression for item in iterable]`  
**Answer:**
```python
squares = [x * x for x in range(1, 6)]
print(squares)
```

---

## Q7. List comprehension with condition – even numbers  
**Hint:** Add `if` condition inside list comp  
**Answer:**
```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```

---

## Q8. Remove duplicates using set  
**Hint:** `set()` removes duplicates  
**Answer:**
```python
fruits = ["apple", "banana", "apple"]
unique_fruits = list(set(fruits))
print(unique_fruits)
```

---

## Q9. Reverse a list using slicing  
**Hint:** `[::-1]` slices backwards  
**Answer:**
```python
reversed_list = nums[::-1]
print(reversed_list)
```

---

## Q10. Clear the list  
**Hint:** `.clear()` removes all elements  
**Answer:**
```python
lst.clear()
```

---

## Q11. Copy the list  
**Hint:** Use `.copy()` for shallow copy  
**Answer:**
```python
new_list = lst.copy()
```

---

## Q12. Basic operations: Length and check existence  
**Hint:** Use `len()` and `in`  
**Answer:**
```python
print(len(lst))        # Size of list
print("pen" in items)  # Membership test
```

---

## Q13. Replace item by index  
**Hint:** Direct assignment using index  
**Answer:**
```python
lst[2] = "new_value"
```

---

## Q14. One-liner with list comprehension  
**Hint:** Powerful one-line transformation  
**Answer:**
```python
["even" for x in range(10) if x % 2 == 0]
```

---
