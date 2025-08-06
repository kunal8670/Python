## ✅ Stage 2: Topic 2 – Lists in Python  
🎯 **Goal**: Master list creation, indexing, slicing, updating, nesting, built-in methods, tricks, and real-world applications.

---

### 🧠 Core Concepts

- `list` = ordered, mutable collection of items.
- Can hold different data types.
- Defined using square brackets `[]`

```python
fruits = ["apple", "banana", "cherry"]
```

---

### 🔢 Indexing & Slicing

```python
fruits[0]        # "apple"
fruits[-1]       # "cherry"
fruits[0:2]      # ["apple", "banana"]
fruits[:2]       # ["apple", "banana"]
fruits[::2]      # ["apple", "cherry"]
```

---

### 🛠️ Important Methods (Mutate List)

```python
append(x)         # Add one element at end
extend(iterable)  # Add multiple items
insert(i, x)      # Insert at position
remove(x)         # Remove by value
pop(i)            # Remove by index
clear()           # Remove all items

index(x)          # Find first index of x
count(x)          # Count occurrences

sort()            # Sort ascending
sort(reverse=True)# Sort descending
reverse()         # Reverse order
copy()            # Return a shallow copy
```

---

### 🧪 Other Useful Functions

```python
len(lst)            # Number of elements
sum(lst)            # Sum of numbers
min(lst), max(lst)  # Smallest/largest values
sorted(lst)         # Returns a new sorted list
enumerate(lst)      # Index-value pairs
list("hello")       # ['h','e','l','l','o']
```

---

### 🔁 Looping Over List

```python
for item in fruits:
    print(item)

for i, item in enumerate(fruits):
    print(i, item)
```

---

### 🔁 List Comprehension

```python
squares = [x**2 for x in range(5)]  
even = [x for x in range(10) if x%2==0]
```

---

### 🧩 Nested Lists

```python
matrix = [[1,2,3], [4,5,6]]
print(matrix[0][1])  # 2
```

---

### 💡 Tricks & One-Liners

```python
# Flatten nested list
flat = [item for sublist in matrix for item in sublist]

# Swap elements
lst[0], lst[1] = lst[1], lst[0]

# Remove duplicates while preserving order
no_dupes = list(dict.fromkeys(lst))

# Reverse list
rev = lst[::-1]

# Slice copy
new = lst[:]
```

---

### ⚠️ Common Mistakes

- `list1 = list2` → same reference. Use `copy()` or slicing to clone.
- `remove(x)` raises error if `x` not found.
- `pop()` without index removes last item.
- `sort()` modifies in-place, use `sorted()` for new sorted version.

---

### 📝 Mini Exercises

1. Add and remove items from a shopping list.
2. Find unique words from a sentence.
3. Track scores of students and sort them.
4. Convert a list of temperatures from °C to °F using list comprehension.
