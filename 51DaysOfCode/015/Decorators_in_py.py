
def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print("This is from wrapper function")
        return original_function(*args, **kwargs)
    return wrapper_function

def display():
    print('This is from display function')

decorated_func = decorator_function(display)

decorated_func()

#Using @ symbol for decorators

@decorator_function
def display2():
    print('This is from Display 2')

@decorator_function
def display3(name, age):
    print(f'This is from Display 3 with ({name} ,{age})')

display3('Nihal', 26)

display2()