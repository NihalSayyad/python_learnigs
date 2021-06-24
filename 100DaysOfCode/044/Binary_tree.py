class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        element = []
        if self.left:
            element += self.left.post_order_traversal()
        if self.right:
            element += self.right.post_order_traversal()

        element.append(self.data)
        return element

    def pre_order_traversal(self):
        element = []
        element.append(self.data)
        if self.left:
            element += self.left.pre_order_traversal()
        if self.right:
            element += self.right.pre_order_traversal()

        return element

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    #print(numbers_tree.search(20))
    #print(numbers_tree.search(22))
    #print(numbers_tree.find_min())
    #print(numbers_tree.find_max())
    #print(numbers_tree.calculate_sum())
    #print(numbers_tree.pre_order_traversal())
    #print(numbers_tree.post_order_traversal())
    print(numbers_tree.delete(17))
    print(numbers_tree.in_order_traversal())