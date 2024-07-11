class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.bst = None

    def insert(self, key):
        if self.bst is None:
            self.bst = TreeNode(key)
        else:
            self._insert(self.bst, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def inorder(self):
        self._inorder(self.bst)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.val, end=" ")
            self._inorder(node.right)

    def search(self, key):
        return self._search(self.bst, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.bst = self._delete(self.bst, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._mon_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    bst.inorder()

    print("\nSearch for 40:", bst.search(40) is not None)
    print("Search for 25:", bst.search(25) is not None)

    bst.delete(20)
    bst.inorder()

    bst.delete(30)
    bst.inorder()

    bst.delete(50)
    bst.inorder()