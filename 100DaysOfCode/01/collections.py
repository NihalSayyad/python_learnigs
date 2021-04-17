''' 
List : Ordered collection of valid datatyps
       mutable
       can contain another list within the same list
'''

list1 = [1,2,3,[4,5,6]]

print(list1)
print(list1[3])

names = ['Ann', 'Bob', 'Craig', 'Diana', 'Eric']

names.insert(1, 'Sia')
print(names)

names.remove('Bob')
print(names)

for element in names:
    print(element , end='----\n')

'''
Tupple : Similar to list, except it is immutable 
'''

ip = ('10:20:30:40', 8080)

print(ip)
print(ip[0])
print(ip[1])

only_one = ()