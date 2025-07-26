#The position of the first occurrence of "Error"
#The position of the last occurrence of "Error"
#Why should you prefer .find() over .index() in risky situations?

note = "Error: failed to connect to database at 10.0.0.1. Error code: 504"
print(note.find('Error'))#of first occurrence "Error"
print(note.rfind('Error'))#of last occurrence of "Error"
print(note.find('kunal'))#if not avlable returns -1
print(note.index('kunal'))#if not avlable returns error ValueError


