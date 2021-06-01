class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end="->")
            curr_node = curr_node.next

    def insert_after_node(self, prev_node, data):

        new_node = Node(data)
        curr_node = self.head
        while curr_node.next.data != prev_node and curr_node.next:
            curr_node = curr_node.next

        if curr_node:
            new_node.next = curr_node.next
            curr_node.next = new_node

    def delete_node(self, key):
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node:
            prev_node.next = curr_node.next
            curr_node = None

    def delete_from_position(self, position):
        curr_node = self.head
        if position == 1:
            self.head = curr_node.next
            curr_node = None
            return


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append('E')
llist.append('F')
llist.print_list()
print("\n-------------------------")

llist.delete_node('A')

llist.print_list()
print("\n-------------------------")
llist.delete_node('C')
llist.print_list()
print("\n-------------------------")
llist.delete_node('F')
llist.print_list()
print("\n-------------------------")
llist.delete_from_position(1)
llist.print_list()