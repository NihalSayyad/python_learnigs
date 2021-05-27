class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def get_stack(self):
        return self.items

s = Stack()
s.push('A')
s.push('B')

print(s.get_stack())