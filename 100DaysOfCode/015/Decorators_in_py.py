
def decorator_function(original_function):

    def wrapper_function():
        print("This is from wrapper function")
        return original_function()
    return wrapper_function

def display():
    print('This is from display function')

decorated_func = decorator_function(display)

decorated_func()