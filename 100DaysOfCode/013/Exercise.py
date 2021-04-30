'''
Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''

lst = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(lst)

'''
Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

out = [{'country':i,'city':j} for row in countries for i, j in row]
print(out)
