
# 🧠 Python Set – Mastery Notes

## ✅ What is a Set?
A `set` is an **unordered collection of unique items** in Python.

```python
# Syntax:
my_set = {1, 2, 3}
another_set = set([1, 2, 2, 3, 4])  # duplicates will be removed
````

---

## 🧱 Key Characteristics of Sets

| Property          | Value                             |
| ----------------- | --------------------------------- |
| Ordered           | ❌ No                              |
| Allows Duplicates | ❌ No                              |
| Mutable           | ✅ Yes                             |
| Indexable         | ❌ No                              |
| Iterable          | ✅ Yes                             |
| Hashable Items    | ✅ Only hashable (int, str, tuple) |

---

## 📌 Syntax and Examples

```python
# Define a set
colors = {"red", "blue", "green"}

# Remove duplicates automatically
numbers = {1, 2, 3, 1, 2}
print(numbers)  # Output: {1, 2, 3}

# Using set() function
unique_chars = set("hello")  # {'h', 'e', 'l', 'o'}
```

---

## 🛠️ Real-World Use Cases

### 1. 🔁 Remove Duplicates from List

```python
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]
unique = set(emails)
```

### 2. ⚡ Fast Membership Testing

```python
blocklist = {"S-999", "S-998"}
if "S-999" in blocklist:
    print("Blocked!")
```

### 3. 🔄 Convert List → Set → List

```python
items = [1, 2, 3, 3, 4]
no_duplicates = list(set(items))
```

---

## 🔧 Set Methods

| Method             | Description                      | Example             |
| ------------------ | -------------------------------- | ------------------- |
| `add(x)`           | Add element `x`                  | `s.add(10)`         |
| `remove(x)`        | Remove `x`, Error if not present | `s.remove(10)`      |
| `discard(x)`       | Remove `x`, No error if missing  | `s.discard(10)`     |
| `clear()`          | Remove all items                 | `s.clear()`         |
| `copy()`           | Return shallow copy              | `s2 = s.copy()`     |
| `pop()`            | Remove & return a random item    | `x = s.pop()`       |
| `update(iterable)` | Add multiple elements            | `s.update([1,2,3])` |

---

## 🔁 Set Operations

| Operation            | Symbol | Description                   |                          |
| -------------------- | ------ | ----------------------------- | ------------------------ |
| Union                | \`     | \`                            | All items from both sets |
| Intersection         | `&`    | Items common to both          |                          |
| Difference           | `-`    | Items only in the first set   |                          |
| Symmetric Difference | `^`    | Items in either, but not both |                          |

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)  # {1, 2, 3, 4}
print(a & b)  # {2, 3}
print(a - b)  # {1}
print(a ^ b)  # {1, 4}
```

---

## 🧪 Practical Exercises

### Task 1 – Remove duplicates

```python
nums = [1, 2, 2, 3, 4, 4]
print(set(nums))  # {1, 2, 3, 4}
```

### Task 2 – Unique Sensor IDs

```python
sensor_logs = [
    ("S-101", "Room-1", 45, True),
    ("S-102", "Room-2", 47, True),
    ("S-101", "Room-1", 48, True),
]

ids = set()
for sid, loc, tmp, crit in sensor_logs:
    ids.add(sid)
print(ids)  # {'S-101', 'S-102'}
```

### Task 3 – Unique Critical Locations

```python
locations = set()
for sid, loc, tmp, crit in sensor_logs:
    if crit:
        locations.add(loc)
print(locations)
```

---

## ⚠️ Common Mistakes

| Mistake                    | Why it's wrong                               |
| -------------------------- | -------------------------------------------- |
| Using `[]` instead of `{}` | `[]` creates a list, not a set               |
| Using `{}` for empty set   | `{}` creates dict. Use `set()` for empty set |
| Assuming order in sets     | Set order is NOT guaranteed                  |
| Adding list/dict to set    | Error – must add only **hashable** items     |

```python
s = set()
s.add([1, 2])  # ❌ TypeError: unhashable type: 'list'
s.add((1, 2))  # ✅ Tuple is allowed
```

---

## 📌 Summary Reminders

* Sets are **unordered**, **unique**, and **mutable**.
* Use sets for fast membership testing and duplicate removal.
* Set methods like `add`, `remove`, `union`, and `intersection` are powerful.
* Don’t expect index or ordering — sets don’t support indexing or slicing.

---

## 💡 Bonus Tips

* Convert list → set → list to remove duplicates and preserve mutable type.
* Use set operations (`|`, `&`, `-`, `^`) to solve logic puzzles easily.
* `discard()` is safer than `remove()` when you're unsure if the item exists.


---
