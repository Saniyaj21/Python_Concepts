
# Exersize-2 faulty calculator 

# design a calculator which currectly solve all the problems except the following ones
# 45*3=555, 56+9=77, 56/6=4
# your program should take operator and two numbers as input from user and then return the result



a=int(input("Enter First Number: "))
b=int(input("Enter Second number: "))
operator=int(input("Enter 1 for Sum: \nEnter 2 for Subtraction: \nEnter 3 for Multiplication: \nEnter 4 for Division: "))
if operator==1:
    if a==56 and b==9:
        result=77
    else:
       result = a+b
    
elif operator==2:
    result = a-b
elif operator==3:
    if a==45 and b==3:
        result=555
    else:
       result = a*b
elif operator==4:
    if a==56 and b==6:
        result=4
    else:
       result = a/b
else:
    print("Enter a valid choice: ")
    result=0

print("Result is =",result)
