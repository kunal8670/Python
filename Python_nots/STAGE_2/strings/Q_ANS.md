# ✅ Python String Topic – All Questions + Answer Hints Summary

---

### Q1 ➤ Take username input, strip spaces, convert to lowercase  
```python
UserName = input("Enter username").strip().lower()
```
✅ Use `.strip()` + `.lower()` to clean and unify input.

---

### Q2 ➤ Strip spaces:
1. Both sides  
2. Left only  
3. Right only  
✅ `.strip()` → both  
✅ `.lstrip()` → left only  
✅ `.rstrip()` → right only

---

### Q3 ➤ Reverse a string  
```python
rtext = text[::-1]
```
✅ Use slicing with negative step `[::-1]`

---

### Q4 ➤ Capitalize/title/swapcase
```python
print(name.title())      # Title Case
print(name.capitalize()) # First letter only
print(name.swapcase())   # Swap upper/lower
```
✅ Great for formatting strings for display.

---

### Q5 ➤ Find positions  
```python
note.find("Error")     # First occurrence
note.rfind("Error")    # Last occurrence
note.find("kunal")     # -1 if not found
note.index("kunal")    # ValueError if not found
```
✅ Use `.find()` to avoid crashes.  
✅ `.index()` if you're sure it's there.

---

### Q6 ➤ Mask a password in a log string  
```python
log.replace("1234", "****")
```
✅ `.replace(old, new)` for text substitution.

---

### Q7 ➤ Join list of words with dash  
```python
"-".join(words)
```
✅ `.join()` combines strings with custom separator.

---

### Q8 ➤ String check methods  
```python
"123".isnumeric()   # True  
"abc123".isalnum()  # True  
"abc".isalpha()     # True  
"   ".isspace()     # True
```
✅ Use to validate user input types.

---

### Q9 ➤ Pad numbers with leading zeros using `zfill()`  
```python
str(num).zfill(5)
```
✅ Convert to string, pad using `.zfill(n)`

---

### Q10 ➤ Align text using `.center()`, `.ljust()`, `.rjust()`  
```python
title.center(11, '*')   # **Welcome**  
title.ljust(11, '*')    # Welcome****  
title.rjust(11, '*')    # ****Welcome
```
✅ Format text with alignment and custom filler.

---

### Q11 ➤ `partition()` vs `split()`  
```python
url.partition("://")  # Tuple → includes separator  
url.split("://")      # List → excludes separator  
```
✅ `partition()` = 3 parts  
✅ `split()` = n parts

---

### Q12 ➤ Extract email name  
```python
name, sep, domain = email.partition("@")
```
✅ Use unpacking with `partition()` to extract parts.

---

### Q13 ➤ Email validation logic  
```python
if email.endswith("@gmail.com") and email.startswith("admin") and "@" in email:
    print("Valid admin Gmail address")
```
✅ Use `and` (not `&`) for logic  
✅ Chain multiple conditions safely

---

### Q14 ➤ Use of `ord()` and `chr()`  
```python
ord('A') → 65  
chr(65)  → 'A'
```
✅ Useful in ASCII manipulations or encodings

---

### Bonus ➤ One-liner to check all in one:
```python
email.startswith("admin") and email.endswith("@gmail.com") and "@" in email
```
✅ Efficient combined condition.

---
