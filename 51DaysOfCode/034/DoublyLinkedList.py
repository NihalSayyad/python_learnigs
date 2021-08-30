class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        itr = self.head
        while itr:
            print(str(itr.data) + " <---> ", end=" ")
            itr = itr.next


    def insert_at_end(self, data1):
        new_node = Node(data1)
        if self.head == None:
            self.head = new_node
            return

        itr = self.head
        prev_node = None
        while itr:
            prev_node = itr
            itr = itr.next

        prev_node.next = new_node
        new_node.prev = prev_node



    def insert_values(self, data):
        for d in data:
            self.insert_at_end(d)


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_values(['A','B','C','D'])
    dll.print()