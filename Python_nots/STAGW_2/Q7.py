#Q7: Character Checking Methods
#These methods check the type of content inside a string:
#.isalpha() → only letters (a–z, A–Z)
#.isalnum() → letters + numbers (no symbols or spaces)
#.isdigit() → only digits
#.isnumeric() → digits + Unicode numbers
#.isdecimal() → only decimal digits (no Unicode)
#.isspace() → only whitespace (' ', '\n', etc.)

 #-->Predict the output of each<--#

print("123".isnumeric())    #True
print("12.3".isnumeric())   #False is an decimal 
print("abc123".isalnum())   #True
print("abc".isalpha())      #True
print("   ".isspace())      #True
