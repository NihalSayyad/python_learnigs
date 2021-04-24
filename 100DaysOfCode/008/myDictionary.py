# key - value pair

from collections import defaultdict, ChainMap
dict1 = {}

print(dict1.get('foo', 'bar'))
print(dict1.setdefault('foo', 'bar'))

print(dict1)

d = defaultdict()
d['key'] = 5

d[1] = 2
print(d)

#Merging two doctionaries
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}

fishdog = {**fish, **dog}

print(fishdog)

fishdog2 = dict(ChainMap(fish, dog))
print(fishdog2)