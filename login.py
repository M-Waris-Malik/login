def reg():
    uname=input("Enter User Name: ")
    upw= input("Enter user Password: ")
    rec={"uName":uname, "uPW":upw}
    registered.append(rec)
    print("You are registered successfuly!")
    print()

def login():
    un=input("User Name: ")
    uc=input("User Code: ")
    found=False
    for i in registered:
        if un==i["uName"] and uc==i["uPW"]:
          found=True
          print("Logged in Successfuly!")  
          break
      
    if found==False:
        print()
        print("Incorrect user name or password!")
        print()
        
registered=[]
while True:
    print("1.Registeration")
    print("2.Login")
    print("0.Exit")
    val=int(input("Enter choice: "))
    print()
    
    if val==1:
        reg()
    elif val==2:
        login()
    elif val==0:
        break
    else:
        print()
        print("Invalid Input!")
        print()