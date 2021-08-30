'''
Imutable data types :
1. int long, float, complex
2. str
3. bytes
4. tupple

Mutable
1. List
2. set
3. dict
'''

a = [1,2,3]

a [0] = 10
a.append(4)
print(a)

b = (1,2,3)

b[0] = 4

'''
Traceback (most recent call last):
  File "e:\Python\100DaysOfCode\python_learnigs\100DaysOfCode\01\Immutable-mutable.py", line 22, in <module>
    b[0] = 4
TypeError: 'tuple' object does not support item assignment
'''