#Q8: Pad numbers using zfill()
#Convert each number into a 5-digit string, padded with leading 0s like this:
#['00042', '00007', '00128']
#str(42).zfill(5)


ids = [42, 7, 128]
#print([str(i).zfill for i in ids ]) #faill one liner
NewLis=[]

for i in ids:
    #print(str(i).zfill(5))  #got it but not an list
    #a=list[str(i).zfill(5)] #for list
    NewLis.append(str(i).zfill(5))
    
#print(a) #faill agan
print(NewLis)    

print([str(i).zfill(5) for i in ids]) #correct one liner 
