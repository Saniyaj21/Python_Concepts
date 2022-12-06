# single inheritence
# YouTube video link - https://www.youtube.com/watch?v=jlvKcnGZdhI

class phone:
    def display(self):
        print("This is a phone class")


class smartPhone(phone):  # derived from base class that is phone
    def show(self):
        print("This is a smartPhone class")


obj1 = smartPhone()  # creating a object of smartPhone class that gives us
# access to the phone class methods also
obj1.display()
obj1.show()
