# Binary Search Tree


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = Node(data, None)

        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)

            else:
                node.left = Node(data, node)

        else:
            if node.right:
                self.insert_node(data, node.right)

            else:
                node.right = Node(data, node)

    def Traverse(self):
        if self.root is not None:
            self.traverse_inorder(self.root)

    def traverse_inorder(self, node):
        if node.left:
            self.traverse_inorder(node.left)

        print(f"{node.data} --> ")

        if node.right:
            self.traverse_inorder(node.right)

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left)

        elif data > node.data:
            self.remove_node(data, node.right)

        else:
            if node.left is None and node.right is None:
                print(f"removing leaf node: {node.data}")

                parent = node.parent

                if parent is not None and parent.left == node:
                    parent.left = None

                if parent is not None and parent.right == node:
                    parent.right = None

                if parent is None:
                    self.root = None

                del node

            elif node.left is None and node.right is not None:
                print(f"removing node which have one child: {node.data}")

                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.right

                    if parent.right == node:
                        parent.right = node.right

                else:
                    self.root = node.right

                node.right.parent = parent
                del node

            elif node.right is None and node.left is not None:
                print(f"removing node which have one child: {node.data}")

                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.left

                    if parent.right == node:
                        parent.right = node.left

                else:
                    self.root = node.left

                node.left.parent = parent
                del node

            else:
                print(f"removing node with two children: {node.data}")

                predecessor = self.get_predecessor(node.left)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)

        return node

    def remove(self, data):
        if self.root is not None:
            return self.remove_node(data, self.root)

    def search(self, data):
        if self.root is None:
            return

        else:
            self.search_node(data, self.root)

    def search_node(self, data, node):

        if node is None:
            return print(f"{data} is not present in BST.\n")

        if data < node.data:
            self.search_node(data, node.left)
        elif data > node.data:
            self.search_node(data, node.right)

        else:
            print(f"{node.data} is present in BST.\n")


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(-5)
    bst.insert(1)
    bst.insert(99)
    bst.insert(34)
    bst.insert(1000)

    bst.search(99)

    bst.Traverse()
