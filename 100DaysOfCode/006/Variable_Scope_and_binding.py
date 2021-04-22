#Nonlocal -- new keyword
#used for the variables which are non-global nad outer scope 

def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

c= counter()
print(c())
print(c())
print(c())

#global variables
#Assignment will happen at the modules's top level, not programs
x = 'Hi'
def change_global_x():
    global x
    x = 'Bye'
    print(x)
change_global_x() # prints Bye
print(x) # prints Bye