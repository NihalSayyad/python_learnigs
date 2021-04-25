
# [ <expression> for <element> in <iterable> if <condition> ]

squares = [ x*x for x in (1,2,3,4) ]

print(squares)

evens  = [x for x in range(10) if x % 2 == 0]
print(evens)

a = (x for x in range(10) if x % 2 == 0)
print(a)