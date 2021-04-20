from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3

print(Color.blue)
print(Color(1))
print(Color['green'])

#Iterating through Enum
print([c for c in Color])

#Output = [<Color.red: 1>, <Color.green: 2>, <Color.blue: 3>]
