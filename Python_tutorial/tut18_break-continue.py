# break and continue


i = 0
while(True):
    if i+1<5:
        i = i+1
        continue  # if if() returns true i will increse and continue will avoid rest of codes 
    print(i+1, end=" ") 
       
    if(i==44):
        break  # if statement returns true break will exit the loop otherwise i will increse
    i=i+1


#exersize
# takes input until user enter a number gratter than 100
while(1):
    number = int(input("\nEnter Your Number: "))
    if number<=100:
        continue
    if number > 100:
        print("You Entered A Number Gratter Than 100 ^-^ : ")
        break
      