# hierarchical inheritance

class parent:
    def display(self):
        print('This is parent class ')
class child_one(parent):
    def show_one(self):
        print('This is child one class ')
class child_two(parent):
    def show_two(self):
        print('This is child two class ')


# both child classes can not access each others methods
obj1 = child_one()  # child one can access to the own class and parent class methods

obj1.display()
obj1.show_one()

print()

obj1 = child_two()  # child two can access to the own class and parent class methods

obj1.display()
obj1.show_two()

