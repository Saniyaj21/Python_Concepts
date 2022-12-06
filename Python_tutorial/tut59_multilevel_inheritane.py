# Multi-Level inheritance

class grandParent:
    def grandShow(self):
        print('This is grnad parent')
        

class parent(grandParent):
    def parentShow(self):
        print('This is parent')
        

class child(parent):
    def childShow(self):
        print('This is child')


obj1 = child()

obj1.childShow()
obj1.parentShow()
obj1.grandShow()