class school:
    def admit(self):
        print(f"Name is {self.name} and roll is {self.roll}")  # self will replace with argument in this case sani

sani = school()
shubha = school()

sani.name = "Saniyaj Mallik"
sani.roll = 2

shubha.name = "Shubhajit Manna"
shubha.roll = 5

sani.admit()   # sani will pass as a argument 

######################## Constructor #################################
class cons:
    def __init__(self, ob_name, ob_roll):
        self.name = ob_name
        self.roll = ob_roll

my_constructor = cons("Rohit", 4)

print(my_constructor.name)