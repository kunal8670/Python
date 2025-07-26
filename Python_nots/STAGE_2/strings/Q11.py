#Q11: Check if an email is valid based on conditions
#Tasks:
#Check if the email starts with "admin"
#Check if the email ends with "@gmail.com"
#Check if the email contains "@"

email = "admin123@gmail.com"
tmp=0

if email.endswith("@gmail.com") and email.startswith("admin") and "@" in email:
    print("Valid admin Gmail address")
else:
    print("Invalid admin Gmail address")
    

