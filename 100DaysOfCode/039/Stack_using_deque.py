from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.container)
print(stack.peek())
print(stack.size())
print(stack.pop())
print(stack.peek())
print(stack.size())

string = 'We will conquere COVID-19'
s1 = Stack()
for ch in string:
    s1.push(ch)
out = ""
while not s1.is_empty():
    out += s1.pop()

print(out)
