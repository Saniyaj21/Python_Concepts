# file opening with block
# it handles the file open and close itself
# so dont need to write this two lines bellow
"""
f = open("sani.txt","rt")

f.close()
"""


# You can do the same work by this, with block handles open and close of files
with open("sani.txt") as f:
    a = f.read()
    print(a)