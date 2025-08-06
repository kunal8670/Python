
# 🧠 Python Dictionary Mastery – Complete Notes

---

## 📌 1. What is a Dictionary?

A **dictionary** is a built-in Python data type that stores data as **key-value pairs**.  
Each key is **unique**, and is used to access its corresponding value.

```python
example = {"name": "Kunal", "age": 21}
````

---

## 📌 2. Why Use a Dictionary?

* When data has **labels** (not positions).
* Useful for **fast lookup** via key.
* Real-world mapping (e.g., name → number, product → price).

---

## 📌 3. Key Features

| Feature             | Detail                                 |
| ------------------- | -------------------------------------- |
| Type                | Built-in, mutable, unordered (pre-3.7) |
| Insertion Ordered   | ✅ Yes (Python 3.7+)                    |
| Mutable             | ✅ Yes (can change/add/delete items)    |
| Keys Must Be Unique | ✅ No duplicate keys allowed            |
| Key Type            | Must be immutable (str, int, tuple)    |
| Value Type          | Can be any type (str, list, dict, etc) |

---

## 📌 4. Dictionary Syntax

```python
# Creating dictionary
data = {
    "name": "Alice",
    "age": 25,
    "is_student": False
}
```

---

## 📌 5. Accessing Values

```python
print(data["name"])          # Alice
print(data.get("age"))       # 25
print(data.get("city"))      # None
print(data.get("city", "N/A"))  # N/A
```

---

## 📌 6. Adding & Updating

```python
data["city"] = "Mumbai"         # Add new
data["age"] = 26                # Update existing
```

---

## 📌 7. Removing Elements

```python
del data["is_student"]         # Delete by key
data.pop("age")                # Removes and returns value
data.clear()                   # Clears the dictionary
```

---

## 📌 8. Useful Dictionary Methods

| Method         | Description                            |
| -------------- | -------------------------------------- |
| `.get(k, def)` | Returns value or default               |
| `.keys()`      | Returns all keys                       |
| `.values()`    | Returns all values                     |
| `.items()`     | Returns key-value pairs                |
| `.update()`    | Merges another dict                    |
| `.pop(k)`      | Removes and returns value              |
| `.popitem()`   | Removes and returns last inserted item |
| `.clear()`     | Clears all items                       |

---

## 📌 9. Looping Through Dictionary

```python
for k in data:
    print(k, data[k])  # key and value

for k, v in data.items():
    print(f"{k} → {v}")
```

---

## 📌 10. Real-World Examples

### 🔹 Count Word Frequency

```python
sentence = "python is fun and python is powerful"
freq = {}

for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)
# {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}
```

---

### 🔹 Grouping Data with setdefault()

```python
students = [("Kunal", "A"), ("Ravi", "B"), ("Priya", "A")]

grade_map = {}
for name, grade in students:
    grade_map.setdefault(grade, []).append(name)

print(grade_map)
# {'A': ['Kunal', 'Priya'], 'B': ['Ravi']}
```

---

### 🔹 Nested Dictionary

```python
students = {
    "S001": {"name": "Kunal", "marks": 88},
    "S002": {"name": "Priya", "marks": 92}
}

print(students["S001"]["marks"])  # 88
```

---

## 📌 11. Dictionary Comprehension

```python
squares = {x: x*x for x in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}
```

---

## 📌 12. Common Mistakes

| Mistake                   | What Happens                 |
| ------------------------- | ---------------------------- |
| Accessing key not in dict | ❌ KeyError                   |
| Using mutable type as key | ❌ TypeError: unhashable type |
| Duplicated key assignment | ✅ Last one overrides earlier |
| Changing dict during loop | ❌ RuntimeError               |

---

## 📌 13. Practice Questions (With Answers)

### Q1: Create a dictionary of squares from 1 to 10

```python
squares = {x: x**2 for x in range(1, 11)}
```

---

### Q2: Count frequency of characters in a string

```python
word = "dictionary"
count = {}

for char in word:
    count[char] = count.get(char, 0) + 1

print(count)
```

---

### Q3: Merge two dictionaries

```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

a.update(b)
print(a)  # {'x': 1, 'y': 3, 'z': 4}
```

---

### Q4: Create dict from two lists

```python
keys = ["name", "age", "city"]
values = ["Kunal", 22, "Mumbai"]

data = dict(zip(keys, values))
```

---

### Q5: Get all unique keys from list of logs

```python
logs = [
    ("S-101", "Room-1", 48.5),
    ("S-102", "Room-2", 35.0),
    ("S-101", "Room-1", 49.0),
    ("S-103", "Room-3", 32.0)
]

unique_ids = {i[0] for i in logs}
```

---

### Q6: Group people by department

```python
data = [
    ("Alice", "IT"),
    ("Bob", "HR"),
    ("Charlie", "IT"),
    ("Diana", "HR"),
    ("Eve", "Sales")
]

grouped = {}
for name, dept in data:
    grouped.setdefault(dept, []).append(name)
```

---

## ✅ 14. Summary – Key Takeaways

* `dict` is **key-value**, not index-based.
* Keys must be **immutable** and **unique**.
* `.get()`, `.items()`, `.setdefault()`, `.update()` are powerful.
* Used in APIs, logs, structured data, config, counting, etc.
* Mastering `dict` = mastering structured data in Python.

---

# 📘 Python Dictionary Methods (Master List)
> ✅ Ranked by real-world usefulness (Top to bottom)  
> 🧠 Includes syntax, use cases, and real examples  
> 🛠 Covers advanced tricks like zip, unpacking, merging, etc.

---

| 🔢 Rank | 🧩 Method / Pattern        | 🧪 Syntax                                      | 💡 Description                                                                 | 🌍 Real-World Use Case                                     | 💻 Example Code |
|--------|----------------------------|-----------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------|----------------|
| 1️⃣    | `get()`                    | `dict.get(key, default)`                      | Returns value or default if key not found                                      | Avoid crashing when accessing optional keys                | `user.get("age", 0)` |
| 2️⃣    | `update()`                 | `dict.update(other)`                          | Merge another dict into current                                                | Overwrite configs, update API response                     | `settings.update(new_conf)` |
| 3️⃣    | `items()`                  | `dict.items()`                                | Returns key-value pairs                                                        | For loop with both key and value                           | `for k, v in d.items():` |
| 4️⃣    | `in` keyword               | `if "key" in dict`                            | Checks for key existence                                                       | Validation, existence checking                             | `if "token" in headers:` |
| 5️⃣    | `setdefault()`             | `dict.setdefault(key, default)`               | Sets value if key not exists                                                   | Grouping, nested dicts                                     | `d.setdefault(k, []).append(v)` |
| 6️⃣    | `pop()`                    | `dict.pop(key, default)`                      | Remove key and return value                                                    | Remove + use entry safely                                  | `data.pop("user", None)` |
| 7️⃣    | `values()`                 | `dict.values()`                               | Returns view of all values                                                     | List/summary operations                                    | `sum(scores.values())` |
| 8️⃣    | `keys()`                   | `dict.keys()`                                 | Returns view of all keys                                                       | Iterating/filtering keys                                   | `for key in d.keys():` |
| 9️⃣    | `copy()`                   | `dict.copy()`                                 | Returns shallow copy                                                           | Backup before editing                                      | `config_copy = config.copy()` |
| 🔟    | `fromkeys()`               | `dict.fromkeys(keys, default)`                | Create dict from keys with same default value                                  | Init flags/forms                                            | `dict.fromkeys(['a', 'b'], False)` |
| 🔁    | `popitem()`                | `dict.popitem()`                              | Removes last inserted key-value (LIFO)                                         | Stack/queue-like usage                                     | `latest = cache.popitem()` |
| 🧮    | Dictionary Comprehension   | `{k: v for k, v in ...}`                      | Make dict from loops with conditionals                                         | Clean transforms, filters                                  | `{k: v for k, v in d.items() if v > 1}` |
| 🔗    | `zip()` with dict          | `dict(zip(keys, values))`                     | Combine two lists into one dict                                                | Parsing structured input                                   | `dict(zip(fields, data))` |
| ⚡     | Dict Merging (3.9+)        | `dict1 | dict2`                               | Merge 2 dicts into new one (Python 3.9+)                                       | Immutable merge                                             | `merged = d1 | d2` |
| 📦    | Dict Unpacking (Pythonic)  | `{**d1, **d2}`                                | Combine/override keys across dicts                                             | Merging, function kwargs                                   | `result = {**base, **new}` |
| 🔍    | `any()` with `values()`    | `any(v > 10 for v in d.values())`             | Check if any value meets condition                                             | Alert triggers, threshold checking                         | `any(temp > 100 for temp in temps.values())` |
| 🔒    | `all()` with `values()`    | `all(v != "" for v in d.values())`            | Check if all fields are filled                                                 | Form validation                                             | `all(form.values())` |
| 🧪    | `dict()` constructor        | `dict([("a", 1), ("b", 2)])`                  | Build dict from tuple pairs                                                    | Structured build                                            | `dict(pairs)` |
| 🌐    | `len(dict)`                | `len(my_dict)`                                | Total key-value pairs                                                          | Size check                                                  | `if len(d) > 10:` |

---

## 🧠 Special Tricks & Real-World Examples

### ✅ Safe Value Access – `.get()`
```python
config = {"theme": "dark"}
print(config.get("lang", "en"))  # en
````

---

### 🔁 Merging Two Dicts – `.update()`

```python
base = {"a": 1, "b": 2}
extra = {"b": 4, "c": 5}
base.update(extra)
# base = {"a": 1, "b": 4, "c": 5}
```

---

### 🔗 From Two Lists – `zip() + dict()`

```python
keys = ["id", "name", "email"]
values = [101, "Kunal", "kunal@example.com"]
user = dict(zip(keys, values))
# {'id': 101, 'name': 'Kunal', 'email': 'kunal@example.com'}
```

---

### ⚙️ Set Default for Grouping

```python
log = [("ERR", 101), ("INFO", 102), ("ERR", 103)]
grouped = {}

for tag, code in log:
    grouped.setdefault(tag, []).append(code)

# {'ERR': [101, 103], 'INFO': [102]}
```

---

### 📦 Merge via `**`

```python
a = {"x": 1}
b = {"y": 2}
combined = {**a, **b}
# {'x': 1, 'y': 2}
```

---

### 🧮 Dict Comprehension Example

```python
nums = [1, 2, 3]
squares = {n: n**2 for n in nums}
# {1: 1, 2: 4, 3: 9}
```

---

## 📘 Best Practices

* ✅ Use `.get()` or `.setdefault()` — avoid `KeyError`
* ✅ Use `update()` to merge safely
* ✅ Use `zip()` when forming from parallel lists
* ✅ Use `{**a, **b}` to merge without overwriting original
* ✅ Use `.items()` + comprehension for filtering
* ⛔ Avoid modifying dict size during iteration

---

