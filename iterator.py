
class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self): #making an object as iterator by returning in a variable
        return self

    def __next__(self): #iterate one by one till 10
        if self.num <=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration #for loop will only ends when there is exception

values = TopTen()

print(values.__next__()) # prints 1
print(next(values)) # prints 2

# Below will print from 3 to 10 as value is already at 2
for i in values:
    print(i)