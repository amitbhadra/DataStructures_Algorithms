__author__='Kalpak Seal'

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
import queue

def full_nodes_in_tree(root):
    if root is None:
        return 0
    q = queue.Queue()
    q.put(root)
    node = None
    count = 0

    while not q.empty():
        node = q.get()
        if node.get_left() is not None and node.get_right() is not None:
            count += 1
        if node.get_left() is not None:
            q.put(node.get_left())
        if node.get_right() is not None:
            q.put(node.get_right())

    return count

def half_nodes_in_tree(root):
    if root is None:
        return 0
    q = queue.Queue()
    q.put(root)
    node = None
    count = 0

    while not q.empty():
        node = q.get()
        if (node.get_left() is None and node.get_right() is not None) or (node.get_left() is not None and node.get_right() is None):
            count += 1
        if node.get_left() is not None:
            q.put(node.get_left())
        if node.get_right() is not None:
            q.put(node.get_right())
    return  count

def leaf_nodes_in_tree(root):
    if root is None:
        return 0
    q = queue.Queue()
    q.put(root)
    node = None
    count = 0

    while not q.empty():
        node = q.get()
        if node.get_left() is None and node.get_right() is None:
            count += 1
        if node.get_left() is not None:
            q.put(node.get_left())
        if node.get_right() is not None:
            q.put(node.get_right())

    return count

if __name__ == '__main__':
    root = BinaryTreeNode(1)

    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)

    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    print ("Number of Full Nodes in the tree: ", full_nodes_in_tree(root))
    print ("Number of Half Nodes in the tree: ", half_nodes_in_tree(root))
    print ("Number of Leaf Nodes in the tree: ", leaf_nodes_in_tree(root))