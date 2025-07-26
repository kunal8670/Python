
## ✅ Stage 2: Topic 1 – Strings in Python

🎯 **Goal**: Master indexing, slicing, methods, tricks, and real-world usages of strings.

---

### 🧠 Core Concepts Recap

**What is a String?**  
- A string in Python is an **immutable** sequence of characters.  
- Defined using single `' '` or double `" "` quotes.

```python
s = "Hello, Python!"
```

---

### 🧩 String Indexing & Slicing

**Indexing**
```python
s = "Python"
print(s[0])     # 'P'
print(s[-1])    # 'n'
```

**Slicing**
```python
s = "Python"
print(s[0:4])    # 'Pyth'
print(s[::2])    # 'Pto'
print(s[::-1])   # 'nohtyP'
```

> 💡 Tip: Negative indexing and slicing are useful for reversing and manipulating parts of strings.

---

### 🧪 Common String Methods

| Method           | Description                            | Example                                 |
|------------------|----------------------------------------|-----------------------------------------|
| `lower()`        | Convert to lowercase                   | `"HELLO".lower()` → `'hello'`           |
| `upper()`        | Convert to uppercase                   | `"hello".upper()` → `'HELLO'`           |
| `strip()`        | Remove whitespace from both ends       | `" hello ".strip()` → `'hello'`         |
| `replace(a, b)`  | Replace `a` with `b`                   | `"hi hi".replace("hi","bye")` → `'bye bye'` |
| `split()`        | Split string into list                 | `"a,b,c".split(",")` → `['a','b','c']`  |
| `join()`         | Join list into string with delimiter   | `".".join(['a','b','c'])` → `'a.b.c'`   |
| `startswith()`   | Check if starts with value             | `"Python".startswith("P")` → `True`     |
| `endswith()`     | Check if ends with value               | `"Python".endswith("n")` → `True`       |
| `find()`         | First index of value                   | `"banana".find("a")` → `1`              |
| `count()`        | Count of value                         | `"banana".count("a")` → `3`             |
| `isalpha()`      | Check if all chars are alphabets       | `"abc".isalpha()` → `True`              |
| `isdigit()`      | Check if all chars are digits          | `"123".isdigit()` → `True`              |

**To print all String all Methods:**
```python
print(dir(str))
```

---

### 🧠 String Formatting Techniques

**Using f-strings (Best)**
```python
name = "Kunal"
age = 21
print(f"My name is {name} and I am {age} years old.")
```

**Using .format()**
```python
print("My name is {} and I am {} years old.".format(name, age))
```

**Using % operator**
```python
print("My name is %s and I am %d years old." % (name, age))
```

---

### 🧠 Useful Tricks & One-Liners

- **Reverse a string**
```python
reversed_str = s[::-1]
```

- **Check if string is palindrome**
```python
def is_palindrome(s):
    return s == s[::-1]
```

- **Clean input (trim and lowercase)**
```python
input_clean = input().strip().lower()
```

- **Word count**
```python
sentence = "this is a test"
print(len(sentence.split()))
```

- **Count letters & digits**
```python
text = "abc123"
print(sum(c.isalpha() for c in text))  # → 3
print(sum(c.isdigit() for c in text))  # → 3
```

- **Convert list to sentence**
```python
words = ['hello', 'world']
sentence = ' '.join(words)
```

---

### 📝 Exercise Ideas

1. Reverse words in a sentence  
   Input: `"Hello world"` → Output: `"world Hello"`

2. Check if string is a palindrome

3. Count vowels, consonants, digits, and special characters

---

### ⚠️ Mistakes to Avoid

- ❌ Trying to modify a string directly: `s[1] = "a"` → Error (strings are immutable)
- ❌ Forgetting to use `.strip()` on input
- ❌ Using `is` instead of `==` for string comparison

---

