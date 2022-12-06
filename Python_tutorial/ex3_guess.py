n = 18

#no of guesses = 9
#print number of guesses left 
#number of gusses he took to finish
# game over

attempt = 0
choice_left = 9
while(1):
    num = int(input("Enter a number to gusse Predifine Number: "))
    attempt = attempt + 1
    choice_left = choice_left - 1
    print("Your Choice Left More : ", choice_left)
    if choice_left<1:
        print("You Lose This Game ^-^\n\n")
        break
    elif num == n:
        print("You Won The Game ^-^ \nThe Number is : ", n ,"\nAnd your total attempt is :",attempt)
        break

    elif num < n:
        print("Tip\tEnter Little Bigger < Number :\n\n")
    else:
        print("Tip\tEnter Little Smaller > Number :\n\n")