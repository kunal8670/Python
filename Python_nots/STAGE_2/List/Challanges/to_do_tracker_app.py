#🔰 Challenge 2: To-Do Task Filter – Real Time Sorting & Status Tracker💼 Scenario:
#You're building a to-do tracker app. Tasks are stored as:
#Your app must:

#Print only pending tasks.
#Allow user to mark a task as done.
#Add new tasks.
#Show tasks grouped by status (done or pending).

#🧠 Task Goals:
#Work with nested lists and string conditions.
#Update inner elements of a list.
#Show filtered/grouped output.

tasks = [["Learn Python", "done"], ["Go to gym", "pending"], ["Write notes", "pending"]]
tmp=0
#pending=([i for i,j in tasks if j=="pending"]) #To fetech all pending task


def ToMark(tasks,Return_From_pending):  #to mark as done  
    a=int(input("Wich task are you want to mark (Enter number)\n>>>"))
    a-=1
    key=Return_From_pending[a]
    #print(Return_From_pending)
    
    for i in range(len(tasks)):
        if tasks[i][0]==key:
            tasks[i][1]="done"
            

def PriPending(tasks): #To print pending task
      pending=([i for i,j in tasks if j=="pending"])
      tmp=0
      if len(pending)!=0:
        for i in pending:   #to print in user like o/p
          tmp+=1
          print(f"{tmp}:{i}")
      else:
          print("You dont have any 'Pending task'\n")
             
      return pending   #onaly writen task not its key 


def AddNewTasks(tasks): #to add new task 
    about=input("Add task Discrption:\n>>>").strip()
    status=input("Enter task status (pending, process, done)\n>>>").lower().strip()
    tasks.append([about,status])
    

def GroupedByStatus(tasks):
    pending=([i for i,j in tasks if j=="pending"])
    done=([i for i,j in tasks if j=="done"])

    tmp1=0
    print("Pending".center(30))
    if len(pending)!=0:
      for i in pending:   #to print in user like o/p
        tmp1+=1
        print(f"{tmp1}:{i}")
    else:
          print("You dont have any 'Pending task'\n")

    print("Done".center(30))

    tmp2=0
    if len(done)!=0:
      for i in done:   #to print in user like o/p
          tmp2+=1
          print(f"{tmp2}:{i}")
    else:
          print("You dont have any 'done task'\n")      


       
    

while True:
    #Return_From_pending=PriPending(tasks)
    a=int(input("Enter 1: for mark as Done task\nEnter 2: for add new task\nEnter 0: to exit\nEnter 3: for Grouped by task>>>"))

    if a==1:
        Return_From_pending=PriPending(tasks)
        ToMark(tasks,Return_From_pending)
    elif a==2:
        AddNewTasks(tasks)
    elif a==3:
        GroupedByStatus(tasks)
    elif a==0:
        print("Have a good day\n")
        break  
    else:
        print("Enlegal input")      
    


#AddNewTasks(tasks)
#Return_From_pending=PriPending(tasks)
#ToMark(tasks,Return_From_pending)
#PriPending(tasks) 









    





