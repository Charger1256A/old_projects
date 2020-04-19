users = {}
status = ""

def displayMenu():
   status = input("Are you a registered user? y/n Press q to quit ")
   if status == "y":
       oldUser()
   elif status == "n":
       newUser()

def newUser():
   createLogin = input("Create Username: ")

   if createLogin in users:
       print("\nLogin name already exists!\n")
   else:
       createPassw= input("Create Password: ")
       users[createLogin] = createPassw
       print("\n User created\n")

def oldUser():
   login = input("Enter Username: ")
   passw = input("Enter Password: ")

   if login in users and users[login] == passw:
       print("\nLogin succesful!\n")
   else:
       print("\nUser doesn't exist or wrong password!\n")
while status != "q":
   displayMenu()
