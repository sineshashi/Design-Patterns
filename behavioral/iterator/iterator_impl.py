'''
Implementing iterator in a b-tree.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MyTree:
    def __init__(self, root):
        self.root = root

    def add_node(self, node):
        current = self.root
        while True:
            if node.val <= current.val:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right
    
    def __iter__(self):
        if self.root is None:
            self.stack = []
        else:
            self.stack = [self.root]
            current = self.root
            while current.left is not None:
                current = current.left
                self.stack.append(current)
        return self

    def __next__(self):
        if len(self.stack)<=0:
            raise StopIteration()

        while len(self.stack) > 0:
            current = self.stack.pop()
            val = current.val
            if current.right is not None:
                current = current.right
                self.stack.append(current)

                while current.left is not None:
                    current = current.left
                    self.stack.append(current)
            return val

tree = MyTree(Node(16))
tree.add_node(Node(8))
tree.add_node(Node(1))
tree.add_node(Node(17))
tree.add_node(Node(13))
tree.add_node(Node(14))
tree.add_node(Node(9))
tree.add_node(Node(10))
tree.add_node(Node(11))
for i in tree:
    print(i)           