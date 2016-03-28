def noempty(f):
    def decorator(self, *args, **kwargs):
        if self.isEmpty():
            raise LookupError("Tree is empty.")
        return f(self, *args, **kwargs)
    return decorator


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

    def delete(self, key):
        """Remove a key/value pair from the tree"""
        raise NotImplementedError()

    def contains(self, key):
        """Does the tree contain a key/value pair with the given key?
        Return true or false.
        """
        return self.get(key) != None

    def isEmpty(self):
        """Return true if the tree is empty, false if it has at least
        one key/value pair.
        """
        return self.root == None

    @noempty
    def minKey(self):
        """Return the smallest key in the tree."""
        return self._mink_at_node(self.root)

    def _mink_at_node(self, node):
        if node.left == None:
            return node.key
        else:
            return self._mink_at_node(node.left)

    @noempty
    def min(self):
        """Return the smallest key/value pair as a tuple."""
        return self._min_at_node(self.root)

    def _min_at_node(self, node):
        if node.left == None:
            return (node.key, node.value)
        else:
            return self._min_at_node(node.left)

    @noempty
    def maxKey(self):
        """Return the largest key in the tree."""
        return self._maxk_at_node(self.root)


    def _maxk_at_node(self, node):
        if node.right == None:
            return node.key
        else:
            return self._maxk_at_node(node.right)

    @noempty
    def max(self):
        """Return the largest key/value pair as a tuple."""
        return self._max_at_node(self.root)

    def _max_at_node(self, node):
        if node.right == None:
            return (node.key, node.value)
        else:
            return self._max_at_node(node.right)

    def floor(self, key):
        """Return the largest key less than or equal to the given key."""
        raise NotImplementedError()

    def ceiling(self, key):
        """Return the smallest key greater than or equal to the given key."""
        raise NotImplementedError()

    def rank(self, key):
        """Return the number of keys less than the given key."""
        return self._rank_at_node(key, self.root)

    def _rank_at_node(self, key, node):
        if node == None:
            return 0
        elif node.key >= key:
            # Eliminate the current node and the right subtree. Return the
            # rank of the left subtree.
            return self._rank_at_node(key, node.left)
        else:  # node.key < key:
            # Accept the entire left subtree and the current node. Also
            # search the right subtree for any additional matches.
            return 1 + _size(node.left) + self._rank_at_node(key, node.right)

    def select(self, k):
        """Return the key of rank k."""
        raise NotImplementedError()

    def deleteMin(self):
        """Remove the lowest key/value pair from the array."""
        raise NotImplementedError()

    def deleteMax(self):
        """Remove the largest key/value pair from the array."""
        raise NotImplementedError()

    def num_between(self, low, high):
        """Number of keys between low and high, inclusive."""
        return _count(self.keys_between(low, high))


    def keys_between(self, low, high):
        """Generator function for the keys between low and high, inclusive.
        In sorted order.
        """
        if high < low:
            raise ValueError("Low key must be less than high key.")
        yield from self._kbtwn_at_node(low, high, self.root)

    def _kbtwn_at_node(self, low, high, node):
        if node == None:
            return
        elif node.key < low:
            # Eliminate the current node and the left subtree. Yield the
            # matching keys from the right subtree.
            yield from self._kbtwn_at_node(low, high, node.right)
        elif node.key >= low and node.key <= high:
            # Can't eliminate any nodes. Yield matching nodes from the
            # left subtree, the current node, and matching nodes from the
            # right subtree.
            yield from self._kbtwn_at_node(low, high, node.left)
            yield node.key
            yield from self._kbtwn_at_node(low, high, node.right)
        elif node.key > high:
            # Eliminate the current node and the right subtree. Yield the
            # matching keys from the left subtree.
            yield from self._kbtwn_at_node(low, high, node.left)


    def keys(self):
        """Generator function for every key in the tree in soted order."""
        yield from map(_key, self._subtree(self.root))

    def items(self):
        """Generator function for key value pairs in the tree, sorted by key."""
        yield from map(_item, self._subtree(self.root))

    def _subtree(self, node):
        if node == None:
            return
        yield from self._subtree(node.left)
        yield node
        yield from self._subtree(node.right)


def _size(node):
    if node == None:
        return 0
    else:
        return node.size


def _key(node):
    return node.key


def _item(node):
    return node.key, node.value


def _count(iterable):
    num = 0
    for i in iterable:
        num += 1
    return num

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

