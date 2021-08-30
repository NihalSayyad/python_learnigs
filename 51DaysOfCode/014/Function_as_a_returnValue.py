def square(x):
    return x * x

def cube(x):
    return x * x * x

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def high_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = high_order_function('square')
print(type(result))
print(result(3))