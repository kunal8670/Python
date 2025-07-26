balance=0.0
iin=-1

while True:
    try:    
        iin=int(input("1. Check Balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit \n-->").strip())
    except:
        print("Invalid input Please select an optinon and enter it's intger")
        continue

    if iin==1:
        print(f"Your Current Balance is:{balance:.2f}$\n")
        
    elif iin==2:
        while True:
            try:
                tmp=float(input("Enter Amount for Deposit -->"))
                if tmp<=0:
                    print("Invalid amount\n")
                elif tmp>0:
                    balance=balance+tmp
                    print(f"Your sussfuly deposit {tmp:.2f}$ \nCurrent balance is:{balance}$\n")
                    tmp=0    
                    break
            except:
                print("Invalid input try agan")
                continue
            
    elif iin==3:
        while True:
            try:
                tmp=float(input("Enter a amount for Withdrow-->"))
                if tmp<=0:
                    print("Invalid amount\n")
                elif tmp>0:
                    
                    if tmp<=balance:
                        balance=balance-tmp
                        print(f"You succefy Withdrow {tmp:.2f}$ \nCurrent Balance is {balance:.2f}$\n")
                        tmp=0
                        break
                    else:
                        print("unsufshint balance try lesser amount\n")
                        
            except:
                print("Invalid input try again\n")
                continue
    elif iin==4:
        print("Thanks to use Good bay".center(60))
        break
    else:
        print("Invalid input")
