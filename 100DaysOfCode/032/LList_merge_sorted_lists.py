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

        prev_node = None
        pos = 1
        while curr_node and pos < position:
            prev_node = curr_node
            curr_node = curr_node.next
            pos +=1

        if curr_node:
            prev_node.next = curr_node.next
            curr_node = None

    def len_iterative(self):
        curr_node = self.head
        count = 0

        while curr_node:
            count +=1
            curr_node = curr_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        curr_1 = self.head
        prev_1 = None
        while curr_1 and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        curr_2 = self.head
        prev_2 = None
        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if curr_1 and curr_2:
            if prev_1:
                prev_1.next = curr_2
            else:
                self.head = curr_2

            if prev_2:
                prev_2.next = curr_1
            else:
                self.head = curr_1

            curr_1.next, curr_2.next = curr_2.next, curr_1.next

        return

    def reverse_iterative(self):
        curr_node = self.head
        prev_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node

    def merge_sorted_lists(self, node2):
        merged_list = LinkedList()
        curr1 = self.head
        curr2 = node2

        while curr1 or curr2:
            if curr2 is None or curr1.data < curr2.data:
                merged_list.append(curr1.data)
                curr1 = curr1.next
            elif curr1 is None or curr2.data < curr1.data:
                merged_list.append(curr2.data)
                curr2 = curr2.next

        merged_list.print_list()

    def merge_sorted(self, node):


llist1 = LinkedList()
llist1.append(1)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.append(10)

llist2 = LinkedList()
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(6)
llist2.append(8)

llist1.print_list()
print("\n---------------------------")
llist2.print_list()
print("\n---------------------------")

llist1.merge_sorted_lists(llist2.head)
