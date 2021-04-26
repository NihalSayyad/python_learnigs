# reversing a list
a = [1,2,3,4,5,6]

print(a[::-1])


lst = ['a','b','c','d','e']

print(lst[::2])

#Shifting a list using slicing
def shift_list( array, s):
    s %= len(array)

    s *= -1

    shifted_array = array[s:] + array[:s]

    return shifted_array

print(shift_list(a, -7))