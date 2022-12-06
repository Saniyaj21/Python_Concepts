var1 = 5
var2 = 80

var3 = int(input("Enter a number: "))
if var1>var3:
    print("Number is smaller than ",var1)
elif var1==var3:
    print("Number is equal to ",var1)    #its a else if statement which is elif in python
else:
    print("number is bigger than ",var1)

list2 = [1, 2, 3, 5]
print(2 in list2)  #return true or flase if 2 is present in list
print(2 not in list2)  #retorn true or false if 2 is not present in list2

if var3 in list2:
    print("number is present in list ")
else:
    print("number is not present in list ")