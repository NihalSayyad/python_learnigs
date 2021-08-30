# the itertools.groupby() method allows developers to group values of an iterable class based on a
# specified property into another iterable set of values

import itertools

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"),("vehicle", "speed boat"), ("vehicle", "school bus")]

dict1 = {}
f = lambda x: x[0]

for key, group in itertools.groupby(sorted(things, key=f), f):
    dict1[key] = list(group)

print(dict1)