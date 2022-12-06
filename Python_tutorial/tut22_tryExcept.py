# Try except exception handling 

from logging import exception


a= input("Enter 1st number: ")
b= input("Enter 2nd number: ")

try:
    print(int(a)+int(b))
except Exception as e:
    print(e)

print("rest of the code will run now::")
