class Decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("This is from decorator class")
        return self.original_function(*args, **kwargs)

@Decorator_class
def display():
    print("This is from display function")

@Decorator_class
def display2(name, age):
    print(f"This is from display2 function with ({name}, {age})")

display()
display2('Nihal', 26)