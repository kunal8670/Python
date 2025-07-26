from datetime import datetime
import getpass

balance=0.0
iin=-1
w=40
pas="1234"
atm=3

while atm>0:
    inpas=getpass.getpass("Enter a Passwoard to accses a bank (password are hiden):-->")

    if inpas==pas:
        print("Accses Grand\n")
        break
    else:
        atm-=1
        print(f"Wrong Passwoard {atm} attempts left")


    if atm==0:
        print("You entered wrong password many time")
        exit()



while True: #main manu
    #inputs handling
    try:
        print("="*w)
        print("Wellcome to Bank".center(w))
        print("="*w)
        
        iin=int(input("1. Check Balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit \n-->".center(w)).strip())
        print("*"*w)
    except:
        print("Invalid input Please select an optinon and enter it's intger")
        continue

    if iin==1:  #for 1st option
        now=datetime.now()
        date=now.strftime("%d-%m-%Y")
        time=now.strftime("%I:%M %p")

        print("\n"+"="*w)
        print("BANK RECEIPT".center(w))
        print("="*w)
        print("Date".ljust(23)+f":{date}")
        print("Time".ljust(23)+f":{time}")
        print("Current Balance".ljust(23)+f":{balance:.2f}$")
        print("="*w)
        print("Thank You for Banking 🏦".center(w))
        print("="*w+"\n")
        #print(f"Your Current Balance is:{balance:.2f}$\n")
        
    elif iin==2:    #for 2nd option
        while True:
            try:
                tmp=float(input("Enter Amount for Deposit -->"))
                if tmp<=0:
                    print("Invalid amount\n")
                elif tmp>0:
                    
                    now = datetime.now()
                    date_str = now.strftime("%d-%m-%Y")
                    time_str = now.strftime("%I:%M %p")

                    balance=balance+tmp
                    print("\n"+"="*w)
                    print("BANK RECEIPT".center(w))
                    print("="*w)
                    print("Transaction Type".ljust(23)+":Deposit")
                    print("Amount Deposit".ljust(23)+f":{tmp:.2f}$")
                    print("Date".ljust(23)+f":{date_str}")
                    print("Time".ljust(23)+f":{time_str}")
                    print("Current Balance".ljust(23)+f":{balance:.2f}$")
                    print("=" * w)
                    print("Thank You for Banking 🏦".center(w))
                    print("=" * w+"\n")
                    #print(f"Your sussfuly deposit {tmp:.2f}$ \nCurrent balance is:{balance}$\n")
                    tmp=0    
                    break
            except:
                print("Invalid input try agan")
                continue
            
    elif iin==3:    #for 3rd option
        while True:
            try:
                tmp=float(input("Enter a amount for Withdrow-->"))
                if tmp<=0:
                    print("Invalid amount\n")
                elif tmp>0:
                    
                    if tmp<=balance:
                        balance=balance-tmp

                        now=datetime.now()
                        date=now.strftime("%d-%m-%Y")
                        time=now.strftime("%I:%M %p")

                        print("\n"+"="*w)
                        print("BANK RECEIPT".center(w))
                        print("="*w)
                        print("Transaction Type".ljust(24)+":Withdrowl")
                        print("Amount Withdrowl".ljust(23)+f":{tmp:.2f}")
                        print("Date".ljust(23)+f":{date}")
                        print("Time".ljust(23)+f":{time}")
                        print("Current Balance".ljust(23)+f":{balance:.2f}$")
                        print("="*w)
                        print("Thank You for Banking 🏦".center(w))
                        print("="*w+"\n")
                        
                        #print(f"You succefy Withdrow {tmp:.2f}$ \nCurrent Balance is {balance:.2f}$\n")
                        tmp=0
                        break
                    else:
                        print("unsufshint balance try lesser amount\n")
                        
            except:
                print("Invalid input try again\n")
                continue
            
    elif iin==4:    #for 4th option
        print("="*w)
        print("Thanks to use Good bay".center(w))
        print("="*w)
        break
    else:
        print("Invalid input")
