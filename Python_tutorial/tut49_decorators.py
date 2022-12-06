# def name():
#     print("Assinging this function to others function.")


# name_2 = name  # assinging function
# name_2()   # calling the function
# name()  # we can call base function also 


def inner1(func):
    def inner2():
        print("Before function execution")
        func()
        print("After function execution")
    return inner2
@inner1
def function_to_be_used():
    print("This is inside of  the function")

# function_to_be_used = inner1(function_to_be_used)  # this is also can use as a alternative of @inner1 

function_to_be_used()