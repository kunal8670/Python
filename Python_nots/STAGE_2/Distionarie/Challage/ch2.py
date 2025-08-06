#Challenge 2: Inventory Restocking System
# 📦 You manage a warehouse.
# There are existing stocks and a new delivery comes in.
# You must merge them and update quantities properly.

# # Existing stock: item → quantity
stock1 = {
    "pen": 10,
    "notebook": 5,
    "eraser": 3
}

# # Incoming shipment: item → quantity
stock2 = {
    "notebook": 4,
    "pencil": 7,
    "pen": 5
}

curentStock={}
# 🧠 Your Task:
# ✅ Combine both stock1 and stock2 into a single dictionary
# ✅ If an item exists in both, sum the quantities
# ✅ If an item exists only in one, keep it as-is
# ✅ Don’t use collections.Counter (only raw dict logic)

# for key in stock1:
#   curentStock[key]=stock1[key]

# for key in stock2:
    
#     if key  in curentStock:
#       tmp=curentStock[key]+stock2[key]
#       curentStock[key]=tmp
#       #count change onaly if key in curentStock

#     else: # if key not in currentStock we add it 
#         curentStock[key]=stock2[key]  
      



# print(curentStock)


##using method-->
stock1 = {"apple": 10, "banana": 5}
stock2 = {"banana": 7, "orange": 3}

# Step 1: Copy stock1 into curentStock
curentStock = stock1.copy()

# Step 2: Merge stock2 into curentStock
for key, value in stock2.items():
    curentStock[key] = curentStock.get(key, 0) + value

print(curentStock)




# curentStock.update(stock1)
# print(curentStock)
# curentStock.update(stock2)
# print(curentStock)
