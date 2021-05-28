from stack import Stack

def div_by_two(number):
    s = Stack()
    while number>0:
        quo = number % 2
        s.push(quo)
        number = number // 2
    out = ''
    while not s.is_empty():
        out = out + str(s.pop())

    return out

number = 242
print(div_by_two(number))