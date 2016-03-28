import unittest
from bst import BST, Node

class BSTTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        self.nodes = {5: 'five', 7: 'seven', 2: 'two', 3: 'three', 1: 'one', 8: 'eight'}
        for k, v in self.nodes.items():
            self.tree.put(k,v)

    def tearDown(self):
        del self.tree
        del self.nodes

    def testPutGet(self):
        for k, v in self.nodes.items():
            self.assertEqual(v, self.tree.get(k))
        for k in [4,6,9]:
            self.assertIsNone(self.tree.get(k))

    def testLen(self):
        self.assertEqual(6, len(self.tree))

    def testMinKey(self):
        self.assertEqual(1, self.tree.minKey())

    def testMin(self):
        self.assertTupleEqual((1, 'one'), self.tree.min())

    def testMaxKey(self):
        self.assertEqual(8, self.tree.maxKey())

    def testMax(self):
        self.assertTupleEqual((8, 'eight'), self.tree.max())

    def testIsEmpty(self):
        self.assertFalse(self.tree.isEmpty())
        self.assertTrue(BST().isEmpty())


class NodeTestCase(unittest.TestCase):
    def testRepr(self):
        node = Node(6, 'six', 1)
        self.assertEqual("Node(6,'six',1)", repr(node))

