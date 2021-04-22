#Nonlocal -- new keyword
#used for the variables which are non-global nad outer scope 

def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

c= counter()
print(c())
print(c())
print(c())