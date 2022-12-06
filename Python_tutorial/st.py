

   # Code Written By CODES BY SANI  :-
print("\n\t\tStory Library Management System By Codes By Sani")

choice =str(input("What you want to do : Write  Read or update a book : ")).lower()



if choice == "write":
   name = input("What is your Story  name : ").upper()
   name2 = name+ ".txt"
  
   story= str(input("Write here : "))
   a=str(("\n\t\t\t"+name+"\n"+story))
   with open (name2,"w") as op:
    op.write(a)
   print("Your Story Published Successfully :--")
    
    
 

if choice == "read":
    Story_name = input("Enter story name to read : ").lower()
    Story_name2 = Story_name + ".txt"

    with open(Story_name2, "r") as op:
        for i in op:
           print(i)


if choice == "update":
    admin_passwors = str(input("Enter Admin password to update books : "))
    set_password = "1234"
    if admin_passwors == set_password:
        Story_name = input("Enter story name to update : ").lower()
        Story_name2 = Story_name + ".txt"
        story_update =str(input("Write to update Story : "))

        with open(Story_name2, "a") as op:
          op.write(story_update)
        print("Update Succesfull :--")
    else:
        print("Wrong Password\t\tAccess Denied :-")
        




           

   
    


