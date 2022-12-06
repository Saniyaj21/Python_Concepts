# Enumerate function

myList = {"Apple", "Banana", "Coconut", "Mango"}
# i =1
# for item in myList:
#     if i%2 is not 0:  #index start from 1 here
#         print(item)
#     i +=1

# Same thing we can do as follows
for index, item in enumerate(myList):
    if index%2==0:  #index start from 0 so ==0
        print(item)


