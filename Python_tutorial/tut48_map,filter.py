


num = ["3", "7", "8", "6"]

num = list(map(int, num))   # map(function, in_which_you_want )  It applies the function on all elements 
print (num[2]+num[3])

sqrt2 = list(map(lambda x : x*x, num))  # map using lambda function
print(sqrt2)

# Filter

mList = [5,7,78,46,34,23]

def bigger(num):
    
    return num<20

mList2 = list(filter(bigger,mList))   # same as map takes function amd itreable like list and we are type casting to list to see the output as a list
print(mList2)

# Reduce 

from functools import reduce   # it have to import to use reduce function

my3 = [1,2,3,4]
num = reduce(lambda x,y:x+y, my3)  # lambda takes x and y and calculate sum of then with itration of my3 list
print(num)















# dic = {"sani":"10", "shubha":"20"}
# s = "sani"
# print(dic[s])