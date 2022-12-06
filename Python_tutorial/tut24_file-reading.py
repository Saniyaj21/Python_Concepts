f = open("sani.txt", "rt")  # rt is mood r is read and t is text format
content = f.read()

#reading using for loop

# for line in f:
#     print(line, end="")


#print(content)

#print(f.readlines())  # print the whole string using \n
# print(f.readline())  # print the first line 
# print(f.readline())  # print the first two lines            


f.close()