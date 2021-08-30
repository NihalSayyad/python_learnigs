class TreeNode:
    def __init__(self, data):
        self.data = data
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

    def print_tree(self, level):
        if self.get_level() <= level:
            spaces = " " * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for i in self.children:
                    i.print_tree(level)

def build_geo_tree():
    root = TreeNode("Global")

    Gujarat = TreeNode("Gujarat")
    Gujarat.add_child(TreeNode("Ahamdabad"))
    Gujarat.add_child(TreeNode("Baroda"))

    Maharashtra = TreeNode("Maharashtra")
    Maharashtra.add_child(TreeNode("Pune"))
    Maharashtra.add_child(TreeNode("Mumbai"))

    India = TreeNode("India")
    India.add_child(Gujarat)
    India.add_child(Maharashtra)

    NJ = TreeNode("New Jersey")
    NJ.add_child(TreeNode("Princeton"))
    NJ.add_child(TreeNode("Trenton"))

    CA = TreeNode("California")
    CA.add_child(TreeNode("San Francisco"))
    CA.add_child(TreeNode("Mountain View"))
    CA.add_child(TreeNode("Palo Alto"))

    USA = TreeNode("USA")
    USA.add_child(NJ)
    USA.add_child(CA)

    root.add_child(India)
    root.add_child(USA)

    return root

if __name__ == "__main__":
    root = build_geo_tree()
    root.print_tree(3)