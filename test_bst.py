import unittest
from bst import BST, Node


class BSTTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        self.nodes = {5: "five", 7: "seven", 2: "two", 3: "three", 1: "one",
                      8: "eight"}
        for k, v in self.nodes.items():
            self.tree.put(k, v)

    def tearDown(self):
        del self.tree
        del self.nodes

    def testPutGet(self):
        for k, v in self.nodes.items():
            self.assertEqual(v, self.tree.get(k))
        for k in [4, 6, 9]:
            self.assertIsNone(self.tree.get(k))

    def testLen(self):
        self.assertEqual(6, len(self.tree))

    def testMinKey(self):
        self.assertEqual(1, self.tree.minKey())

    def testMin(self):
        self.assertTupleEqual((1, "one"), self.tree.min())

    def testMaxKey(self):
        self.assertEqual(8, self.tree.maxKey())

    def testMax(self):
        self.assertTupleEqual((8, "eight"), self.tree.max())

    def testIsEmpty(self):
        self.assertFalse(self.tree.isEmpty())
        self.assertTrue(BST().isEmpty())

    def testItems(self):
        self.assertSequenceEqual(sorted(self.nodes.items()),
                                 list(self.tree.items()))

    def testKeys(self):
        self.assertSequenceEqual(sorted(self.nodes.keys()),
                                 list(self.tree.keys()))

    def testContains(self):
        self.assertTrue(self.tree.contains(8))
        self.assertFalse(self.tree.contains(13))

    def testKeysBetween(self):
        self.assertSequenceEqual([2, 3, 5], list(self.tree.keys_between(2, 6)))

    def testNumKeysBetween(self):
        # self.nodes = {5: 'five', 7: 'seven', 2: 'two', 3: 'three', 1: 'one',
        # 8: 'eight'}
        self.assertEqual(4, self.tree.num_between(3, 8))

    def testRank(self):
        self.assertEqual(2, self.tree.rank(3))


class NodeTestCase(unittest.TestCase):
    def testRepr(self):
        node = Node(6, "six", 1)
        self.assertEqual("Node(6,'six',1)", repr(node))
