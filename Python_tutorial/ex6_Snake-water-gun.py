#snake water gun

"""
win system --
sanke-water = sanke
water-gun = water
snake-gun = gun
"""
import random

round_game = 0
com_score =0
user_score =0

print("\t\t\nWelcome to Snake Water Gun Game : ")
while(round_game<10):
    print("\nEnter your choice : ")
    choice = int(input("Enter 1 For Snake:  2 For Water:  3 For Gun: "))
    if choice == 1:
        take_name = "Snake"
    elif choice == 2:
        take_name ="Water"
    elif choice == 3:
        take_name = "Gun"

    lst = ["Snake", "Water", "Gun"]
    choice_com = random.choice(lst)
    
    

    #  For draw
    if choice == 1 and choice_com == "Snake" or choice == 2 and choice_com == "Water" or choice == 3 and choice_com == "Gun":
        y=f"Game drow :\n You both chose : {choice_com}"
        print(y)
        round_game+=1
    # For user wining    
    elif choice == 2 and choice_com == "Gun" or choice == 1 and choice_com == "Water" or choice == 3 and choice_com == "Snake":
        round_game+=1
        user_score+=1       
        print(f"Computer choice is : {choice_com}\t And Your choice is : {take_name}")
        print("User Won The round : User score is : ",user_score,end="\n")

    elif choice == 1 and choice_com == "Gun" or choice == 2 and choice_com == "Snake" or choice == 3 and choice_com == "Water":
       
        round_game+=1
        com_score+=1        
        print(f"Computer choice is : {choice_com}\t And Your choice is : {take_name}")        
        print("Computer Won The Round : Computer score is : ",com_score,end="\n")

x = f"Computer score is : {com_score}\t And User score is : {user_score}"
print(x)
if com_score>user_score:

    print("Computer Won the Game : \n")
elif com_score==user_score:
    print("Match Drow : ")
else:
    print("User Won the Game : \n") 

