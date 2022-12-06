


# Youtube video - https://www.youtube.com/watch?v=HfmFcj0NmHI&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=66

class parent:
    name = "Sani"
    def __init__(self):
        self.roll=12
        self.sub="programming"
        self.special = "This is special"

class child(parent):
    name = "Rohit"
    def __init__(self):
        super().__init__()  # this call first parent class constructor then bellow two lines will override again
        self.roll = 30
        self.sub = "Computer"
        # super().__init__()   if we use super after overriding it will go parent class change the value of variable

a = parent()
b = child()


print(b.special, b.sub, b.roll)