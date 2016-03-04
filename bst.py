
class BST(object):
    def __init__(self):
        self.root = None

    def __len__(self):
        if self.root == None:
            return 0
        return self.root.size

    def get(self, key):
        """Return the value associated with a key.
        If no key is present, return None.
        """
        return self._get_at_node(key, self.root)

    def _get_at_node(self, key, node):
        if node == None:
            return None
        if key < node.key:
            return self._get_at_node(key, node.left)
        elif key > node.key:
            return self._get_at_node(key, node.right)
        else:  # key == node.key
            return node.value
        
    def put(self, key, value):
        """Insert a key-value pair into the tree.
        If the key is already present, replace its value with the one given.
        """
        self.root = self._put_at_node(key, value, self.root)

    def _put_at_node(self, key, value, node):
        if node == None:
            return Node(key, value, 1)
        if key < node.key:
            node.left = self._put_at_node(key, value, node.left)
        elif key > node.key:
            node.right = self._put_at_node(key, value, node.right)
        else:  # key == node.key
            node.value = value
        node.size = _size(node.left) + _size(node.right) + 1
        return node

def _size(node):
    if node == None:
        return 0
    else:
        return node.size

class Node(object):
    def __init__(self, key, value, size):
        self.key = key
        self.value = value
        self.size = size
        self.left = None
        self.right = None

if __name__ == '__main__':
    tree = BST()
    for k, v in [(5, 'five'), (7, 'seven'), (2, 'two'), (3, 'three'), (1, 'one'), (8, 'eight')]:
        tree.put(k, v)

    print('length:', len(tree))
    print(tree.root.key)
    print(tree.root.value)

    for n in range(10):
        print('get({0}): {1}'.format(n, tree.get(n)))

