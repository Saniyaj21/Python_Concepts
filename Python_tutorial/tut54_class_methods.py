

# Class method is use to change the cals  variable value with objects

class school:
    total_student = 100
    def admit(self):
        print(f"Name is {self.name} and roll is {self.roll}")  # self will replace with argument in this case sani

    @classmethod
    def stdTotal(cls, newTotal):   # this method will take new value from objects and chance the class value
        cls.total_student = newTotal   # cls is like self, it takes as a argument form objects 

sani = school()
shubha = school()

sani.name = "Saniyaj Mallik"
sani.roll = 2

shubha.name = "Shubhajit Manna"
shubha.roll = 5

shubha.admit()


sani.stdTotal(200)   # changing the value with object.method_name(Value)
print(sani.total_student)  # accessing with object.class variable