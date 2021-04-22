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

#locals() globals()

print(globals().keys())
print(locals().keys())

print('--------------------------------------------------------------------------------')

def f1():
    bar = 1
    def f2():
        baz = 2
        # here, foo is a global variable, baz is a local variable
        # bar is not in either scope
        print(locals().keys()) # ['baz']
        print('bar' in locals()) # False
        print('bar' in globals()) # False
        return f3()
 
    def f3():
        baz = 3
        print(bar) # bar from f1 is referenced so it enters local scope of f3 (closure)
        print(locals().keys()) # ['bar', 'baz']
        print('bar' in locals()) # True
        print('bar' in globals()) # False
        return f4()

    def f4():
        bar = 4 # a new local bar which hides bar from local scope of f1
        baz = 4
        print(bar)
        print(locals().keys()) # ['bar', 'baz']
        print('bar' in locals())

    return f2()

print(f1())
