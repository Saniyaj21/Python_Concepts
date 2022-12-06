"""
*
* *
* * *
* * * *

"""
line = int(input("How many rows you want : "))
choice = int(input("Enter 0 or 1 : "))

if choice == 1:
    for i in range(line):
        for j in range(i+1):
            print("*", end=" ")
        print()

if choice == 0:
    for i in range(line):
        for j in range(i, line):
            print("*", end=" ")
        print()



# patterns

for i in range(line):
    for j in range(i, line):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

print()





for i in range(line):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, line):
        print("*", end=" ")
    print()

print()






for i in range(line):
    for j in range(i, line):
        print(" ", end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

print()





for i in range(line):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, line):
        print("*", end=" ")
    for j in range(i, line-1):
        print("*", end=" ")
    print()

print()





for i in range(line-1):
    for j in range(i, line):
        print(" ", end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(line):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, line-1):
        print("*", end=" ")
    for j in range(i, line):
        print("*", end=" ")
    print() 

