'''
Two methods with same method name and arguments but in seperate classes
Ovverrides in sub-class if subclass has this method
Ovverrides in super class if subclass doenst have this method
'''

class A:
    def show(self):
        print("In A show")

class B(A):

    def show(self):
        print("In B show")


a1 = B()
a1.show()