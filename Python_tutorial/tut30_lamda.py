# Lambda function or anonymous function





minus = lambda x, y: x- y   #  this a one line syntax for functions


# Same thing it will do as lambda do
#  
# def minus(x,y):
#     return x-y



print(minus(5, 2))

a = [[5,40],[2,6],[8,23]]  # This is a list of list
a.sort()  # This will sort the list on the basis of 0 index
print(a)
a.sort(key=lambda x:x[1])  # This will sort the list on the basis of 1 index  that is 40 here and key takes a function to work
                                # lambda creates a function key
print(a)