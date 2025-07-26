#Q6: .join() — The “reverse split”
#o/p--> Welcome-to-Python-World


words = ["Welcome", "to", "Python", "World"]#90% correct 
for i in words:
    print(i,end="-")
    

a="-".join(words)#proper 
print("\n"+a)
