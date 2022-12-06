class employee1:
      def __init__(self, name, age):
            self.name=name
            self.age=age

emp = employee1("Sani", 23)
print(emp.age)

class employee2:
      def __init__(self, name, age):
            self._name=name # protected attribute 
            self._age=age # protected attribute

emp2 = employee2("Shubha", 43)
print(emp2._age)

class employee3:
      def __init__(self, name, age):
            self.__name=name # private attribute 
            self.__age=age # private attribute

emp3 = employee3("Rohit", 33)
print(emp3._employee3__age)            


