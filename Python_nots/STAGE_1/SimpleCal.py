print("*****************wellcome to my simple calculater***************")
a=-1
while a!=0:

    a=int(input("Enter 1: for add\nEnter 2: for sub\nEnter 3: for mult\nEnter 4: for dev\nEnter 0: for exit\n-->"))
    if a==0:
        print("***************You are exited from manu**************")
        break
    elif a>4:
        print("Invalid input1")
    else:
        b,c=map(int,input("Enter a two numbers for calcult\n-->").split(' '))
    
    if a==1:
        print("Add of",b,"&",c,"is -->",b+c)
    elif a==2:
        print("Sub of",b,"&",c,"is -->",b-c)
    elif a==3:
        print("Mul of",b,"&",c,"is -->",b*c)
    elif a==4:
        if c==0:
            print("Conot devide by zero")
        else:
            print("Dev of",b,"&",c,"is -->",b/c)
    
