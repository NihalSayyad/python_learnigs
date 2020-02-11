class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None

class LinkedList:
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)
		
		if self.head is None:
			self.head = new_node
			return

		last_node = self.head
		while last_node.next:
			last_node = last_node.next

		last_node.next = new_node

	def print_list(self):
		curr_node = self.head
		while curr_node:
			print(curr_node.data)
			curr_node = curr_node.next

	def prepend(self, data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self, prev_node, data):
		if not prev_node:
			print("Previous node is not present in the list")
			return

		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def delete_node(self, key):

		curr_node = self.head
		if curr_node and curr_node.data == key:
			self.head = curr_node.next
			curr_node=None
			return

		prev = None
		while curr_node and curr_node.data != key:
			prev = curr_node
			curr_node = curr_node.next

		if curr_node is None:
			print("Element is not present")
			return

		prev.next = curr_node.next
		curr_node = None

	def  delete_node_position(self, pos):
		curr_node = self.head
		if curr_node and pos == 1:
			self.head = curr_node.next
			curr_node = None
			return

		prev = None
		index = 1
		while curr_node and pos>index:
			prev = curr_node
			curr_node = curr_node.next
			index += 1

		if curr_node is None:
			print(f"{pos} Position is not present")
			return

		prev.next = curr_node.next
		curr_node = None

	def len_iterative(self):
		count=0
		curr_node = self.head
		while curr_node:
			count += 1
			curr_node = curr_node.next

		print(f"Total node : {count}")
		
	def  len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)

	def swap_nodes(self, key_1, key_2):

		if key_1 == key_2:
			return

		prev_1 = None
		curr_1 = self.head
		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1
			curr_1 = curr_1.next

		prev_2 = None
		curr_2 = self.head
		while curr_2 and curr_2.data != key_2:
			prev_2 = curr_2
			curr_2 = curr_2.next

		#print(f" prev2.data {prev_2.data}")

		if not curr_1 or not curr_2:
			print("One of the key is not present in the list")
			return

		if prev_1:
			prev_1.next = curr_2
		else:
			self.head = curr_2

		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1

		curr_1.next, curr_2.next = curr_2.next, curr_1.next

		

llist = LinkedList()
llist.len_iterative()
print("-------------")
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")


llist.print_list()

print("-------------")

llist.len_iterative()

print(llist.len_recursive(llist.head))
#llist.insert_after_node(llist.head.next,"E")
#llist.delete_node_position(1)
#llist.print_list()
#print("-------------")
#llist.delete_node_position(2)
#llist.print_list()

llist.swap_nodes("E","C")
print("--------------")
llist.print_list()