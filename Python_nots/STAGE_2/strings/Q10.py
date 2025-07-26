# Q10: Split a string into 3 parts using partition()

url = "https://www.google.com"
print(url.partition("://")) #thy devide from parameter in print include parmeter
print(url.split("://")) #seprate from give parameter in print not include 

mail="kkunalhpatil.8670@gmail.com"

a,b,c=mail.partition("@") #assing name for each part to access spacfic data
print(a)


#| Use Case                                | Use `.partition()`            | Use `.split()`            |
#| --------------------------------------- | ----------------------------- | ------------------------- |
#| Extract single separator & keep it      | ✅ Yes (clean slicing)         | ❌ No (drops separator)    |
#| Break string into **more than 3 parts** | ❌ No (only 3 items)           | ✅ Yes (all parts as list) |
#| Need tuple assignment                   | ✅ Great for structured unpack | ❌ Not reliable            |
