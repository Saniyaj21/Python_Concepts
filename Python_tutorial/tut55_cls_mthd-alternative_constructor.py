

######################## Constructor #################################
class cons:
    def __init__(self, ob_name, ob_roll):
        self.name = ob_name
        self.roll = ob_roll


    ##################### class method as alternative constructor ###############

    @classmethod
    def from_dash(cls, string):
        line = string.split("-")
        return cls(string[0], string[1])
        # return cls(*string.split("-"))  one liner of the above two lines

        # End

my_constructor = cons("Rohit", 4)  # constructor

print(my_constructor.name)


# class method as alternative constructor
romes = cons.from_dash("Romes-10")  

print(romes.name,romes.roll)



