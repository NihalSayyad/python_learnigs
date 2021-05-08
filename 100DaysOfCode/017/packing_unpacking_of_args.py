'''
Unpacking lists
'''

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1,2,3,4,5]
print(sum_of_five_nums(*lst))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7


'''
Packing Lists
'''

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

'''
Spreading in python
'''

lst_one = [1,2,3]
lst_two = [4,5,6]

lst = [0, *lst_one, *lst_two]
print(lst)