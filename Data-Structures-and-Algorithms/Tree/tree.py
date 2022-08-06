class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    count = 0
    leave_count = 0

    # root = Node(None)

    def __init__(self, root=None):
        self.root = None

    def add_node(self, data):
        if self.root:
            BinaryTree.count += 1
            return self.add_recursively(self.root, data)
        else:
            BinaryTree.count += 1
            self.root = Node(data)
            return True

    def add_recursively(self, root, data):
        if root.data == data:  # The data is already there
            return False
        elif data < root.data:  # Go to left root
            if root.left:  # If left root is a node
                return self.add_recursively(root.left, data)
            else:  # left root is a None
                root.left = Node(data)
                return True
        else:  # Go to right root
            if root.right:  # If right root is a node
                return self.add_recursively(root.right, data)
            else:
                root.right = Node(data)
                return True

    def in_order_traversal(self, root, traversal=""):
        if root:
            traversal = self.in_order_traversal(root.left, traversal)
            traversal += (str(root.data) + "-")
            traversal = self.in_order_traversal(root.right, traversal)
        return traversal

    def post_order_traversal(self, root, traversal=""):
        if root:
            traversal = self.post_order_traversal(root.left, traversal)
            traversal = self.post_order_traversal(root.right, traversal)
            traversal += (str(root.data) + "-")
        return traversal

    def pre_order_traversal(self, root, traversal=""):
        if root:
            traversal += (str(root.data)+ "-")
            traversal = self.pre_order_traversal(root.left, traversal)
            traversal = self.post_order_traversal(root.right, traversal)
        return traversal

    def print_tree(self, traversal_type):
        if traversal_type == "in_order":
            print(self.in_order_traversal(self.root))
        if traversal_type == "post_order":
            print(self.post_order_traversal(self.root))
        if traversal_type == "pre_order":
            print(self.pre_order_traversal(self.root))


if __name__ == '__main__':
    mti_yetu = BinaryTree()
    mti_yetu.add_node(10)
    mti_yetu.add_node(5)
    mti_yetu.add_node(20)
    mti_yetu.add_node(15)
    mti_yetu.add_node(26)
    mti_yetu.add_node(1)
    mti_yetu.add_node(8)
    mti_yetu.add_node(50)
    mti_yetu.add_node(45)
    mti_yetu.print_tree("in_order")
    mti_yetu.print_tree("post_order")
    mti_yetu.print_tree("pre_order")
    print(mti_yetu.count)
    # print(mti_yetu)
