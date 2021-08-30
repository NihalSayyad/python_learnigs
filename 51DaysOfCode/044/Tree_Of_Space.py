import random

class LockingBinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self._is_locked = False
        self.locked_descendant = 0

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = LockingBinaryTree(data)

        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = LockingBinaryTree(data)

    def _can_lock_or_unlock(self):
        if self.locked_descendant > 0:
            return False

        curr = self.parent
        while curr:
            if curr._is_locked:
                return False
            curr = curr.parent
        return True

    def is_locked(self):
        return self._is_locked

    def lock(self):
        if self._can_lock_or_unlock():

            self._is_locked = True

            curr = self.parent
            while curr:
                curr.locked_descendant += 1
                curr = curr.parent
            return True
        else:
            return False

def build_Tree():
    root = LockingBinaryTree(100)
    for i in range(50):
        root.add_child(random.randint(1,100))

    return root

if __name__ == '__main__':
    root = build_Tree()
    print(root)



