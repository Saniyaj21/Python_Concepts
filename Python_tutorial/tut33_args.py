# args and kwargs
from unicodedata import name


def use_of_args(*args):  # t *args is use for taking multiple argumens as touple  * and name is your choice args not necessary
    """
    Purpose: 
    """
    for i in args:  # printing the touple
        print(i)
    
    
# end def
name = ["sani", "Shubha", "rohit", "raju", "programmer"]
use_of_args(*name)  # * and argument in this case name 

