class TreeNode:
    def __init__(self, data):
        self.name = data[0]
        self.designation = data[1]
        self.children = []
        self.parent = None

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,option):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if option == 'both':
            print(prefix + self.name +'(' + self.designation + ')')
        elif option == 'name':
            print(prefix + self.name)
        elif option == 'designation':
            print(prefix + self.designation)
        if self.children:
            for i in self.children:
                i.print_tree(option)

def build_management_tree():
    root = TreeNode(('Nilupul', 'CEO'))
    root.add_child(TreeNode(('Chinmay','CTO')))
    root.add_child(TreeNode(('Gels', 'HR Head')))

    root.children[0].add_child(TreeNode(('Vishwa','Infra Head')))
    root.children[0].add_child(TreeNode(('Amir', 'Application Head')))

    root.children[0].children[0].add_child(TreeNode(('Dhaval', 'Cloud Manager')))
    root.children[0].children[0].add_child(TreeNode(('Dhaval', 'Cloud Manager')))

    root.children[1].add_child(TreeNode(('Peter', 'Recruitment Manager')))
    root.children[1].add_child(TreeNode(('Waqas', 'Policy Manager')))

    return root

if __name__ == '__main__':
    root = build_management_tree()
    root.print_tree('both')
    print("---------------------------------")
    root.print_tree('name')
    print("---------------------------------")
    root.print_tree('designation')