import unittest
from bst import BST, Node

class BSTTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        self.nodes = {5: 'five', 7: 'seven', 2: 'two', 3: 'three', 1: 'one', 8: 'eight'}
        for k, v in self.nodes.items():
            self.tree.put(k,v)

    def testPutGet(self):
        for k, v in self.nodes.items():
            self.assertEqual(v, self.tree.get(k))
        for k in [4,6,9]:
            self.assertIsNone(self.tree.get(k))

    def testLen(self):
        self.assertEqual(6, len(self.tree))


class NodeTestCase(unittest.TestCase):
    def testRepr(self):
        node = Node(6, 'six', 1)
        self.assertEqual("Node(6,'six',1)", repr(node))

