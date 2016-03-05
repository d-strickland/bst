
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

    def delete(key):
        """Remove a key/value pair from the tree"""
        raise NotImplemented()

    def contains(key):
        """Does the tree contain a key/value pair with the given key?
        Return true or false.
        """
        raise NotImplemented()

    def isEmpty(key):
        """Return true if the tree is empty, false if it has at least
        one key/value pair.
        """
        raise NotImplemented()

    def minKey():
        """Return the smallest key in the tree."""
        raise NotImplemented()

    def min():
        """Return the smallest key/value pair as a tuple."""
        raise NotImplemented()

    def maxKey():
        """Return the largest key in the tree."""
        raise NotImplemented()

    def max():
        """Return the largest key/value pair as a tuple."""
        raise NotImplemented()

    def floor(key):
        """Return the largest key less than or equal to the given key."""
        raise NotImplemented()

    def ceiling(key):
        """Return the smallest key greater than or equal to the given key."""
        raise NotImplemented()

    def rank(key):
        """Return the number of keys less than the given key."""
        raise NotImplemented()

    def select(k):
        """Return the key of rank k."""
        raise NotImplemented()

    def deleteMin():
        """Remove the lowest key/value pair from the array."""
        raise NotImplemented()

    def deleteMax():
        """Remove the largest key/value pair from the array."""
        raise NotImplemented()

    def size(low, high):
        """Number of keys between low and high, inclusive."""
        raise NotImplemented()

    def keys(low, high):
        """Generator function for the keys between low and high, inclusive.
        In sorted order.
        """
        raise NotImplemented()

    def keys():
        """Generator function for every key in the tree in soted order."""
        raise NotImplemented()

    def items():
        """Generator function for key value pairs in the tree, sorted by key."""
        raise NotImplemented()

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

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return 'Node({k},{v},{s})'.format(k=repr(self.key),
                v=repr(self.value), s=repr(self.size))


if __name__ == '__main__':
    tree = BST()
    for k, v in [(5, 'five'), (7, 'seven'), (2, 'two'), (3, 'three'),
                (1, 'one'), (8, 'eight')]:
        tree.put(k, v)

    print('length:', len(tree))
    print(tree.root)

    for n in range(10):
        print('get({0}): {1}'.format(n, tree.get(n)))

