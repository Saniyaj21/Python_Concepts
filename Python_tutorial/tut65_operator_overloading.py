# operator overloading

class Employee:
   

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole



    def __add__(self, other):  # add operator overloading
        return self.salary + other.salary

    def __truediv__(self, other):  # division operator overloading
        return self.salary / other.salary

emp1 =Employee("Harry", 345, "Programmer")
emp2 =Employee("Rohan", 55, "Cleaner")

print(emp1+emp2)  # using operator overloading

