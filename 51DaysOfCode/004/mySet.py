a = {1,2,3,4,5}
b = {4,5,6}

print(a.intersection(b))
print(a.union(b))
print(a.difference(b))


#multi set operations
#Counter from collection will not keep ordering, but keeps the count
from collections import Counter

counterA = Counter(['a','b', 'c','b'])

print(counterA)