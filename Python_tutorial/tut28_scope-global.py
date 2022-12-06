l = 10  #global variable

def function1(n):
    lokl = 5  #local variable
    # l = l + 40 it will throw error if we try to change the value of global variable
    global l  # global is use to change the value of global variable 
    l = l+15
    print(l)
    m = 8
    print(lokl, m)
    print(n," I have printed")

function1("This is me")
# print(m)  # it will throw error becaube it is a local veriable cant be print in global


def sani():
    x = 10  # this is local variable  not global for shubha
    def shubha():
        global x  # it will search global variable x which is not present out of function
        x = 100  # so it will create a global x because global x was not present and assign the value of 100
    print(x)
    shubha()  #calling Shubha inside sanii function
    print(x)
sani()  
print(x)  # this will print the value of x which is created as global variable     


