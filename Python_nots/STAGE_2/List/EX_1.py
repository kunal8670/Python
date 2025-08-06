shopping_list = []

# Adding items
shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs")

print("Shopping List:", shopping_list)  # ['Milk', 'Bread', 'Eggs']

# Removing an item by value
shopping_list.remove("Bread")  

# Removing last item
last_item = shopping_list.pop()

print("Final List:", shopping_list)     # ['Milk']
print("Removed item:", last_item)       # Eggs
