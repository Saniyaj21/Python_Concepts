# object introspetion is nothing but viewing the object details

class Sani:
    def __init__(self,name):
        self.name = name
    
    @property
    def details(self):
        print(self.name)

Student = Sani("Saniyaj")
print(Student.details)  # not using Student.details() because of property decoretor
# now the object introspection
print(type(Student))  # show the type of the object
print(id(Student))  # show object id
print(dir(Student))  # show all functions ans variables

# we have inspect module also for object inspection