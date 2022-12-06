# Operators in Python

#arithmatik operators
print("40 + 5 =", 40+5)
# print("40 - 5 =", 40-5)
# print("40 * 5 =", 40*5)
# print("40 / 5 =", 40/5)
# print("41 % 5 =", 41%5)  # Print the integer value of the division 
# print("40 // 5 =", 40//5)  #print the intiger value of the division
# print("40 ** 5 =", 40**5)  # here 5 is the power of 40

#assignment operators

a=5  #assing the value in a
a +=3
# a -=3
# a /=2
# a *=3
print("Value of a is : ",a)

# comparison operators

print(a==4, "Comparison operator")
# print(a!=4)
# print(a<=4)
# print(a>=4)

# Logical operators

a1=True
b1=False
print(a1 and b1,"Logical Operator")   # and operator
# print(a1 or b1)   # and operator
# print(not a1)

# Identity operator
#print(5 is 5)  # Print true because 5 = 5
print(5 is not 5,"Identity Operator")  # Print false because 5 != 5

#Membership Operator
# --- in and not in ----
my_list=[2, 4, 5, 21, 23, 21]
print(21 in my_list, "Membership operator")
# print(21 not in my_list, "Membership operator")

# Bitwise operators
# 0 = 00 
# 1 = 01
# 2 = 10 
# 3 = 11 
print(1 & 2)
print(1 | 2)