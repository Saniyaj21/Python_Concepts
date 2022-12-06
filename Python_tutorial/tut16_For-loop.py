list2 = ["Sani", "Shubha", "Rohit"]   #list printing using for loop

for i in list2:
    print(i)

list3 = [["sani", 1],  ["Shubha",2], ["Rohit",6]]  # list of list
for item, lolipop in list3:
    print(item, lolipop)

dict2 = dict(list3)  #type casting list to dictionary
for item, lolipop in dict2.items():  # .items() use to access items with its value
    print(item, "and lolipop is ", lolipop)