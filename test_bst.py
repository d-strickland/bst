import unittest
from bst import BST

class BSTTestCase(unittest.TestCase):
    def testPutGet(self):
        tree = BST()
        nodes = {5: 'five', 7: 'seven', 2: 'two', 3: 'three', 1: 'one', 8: 'eight'}
        for k, v in nodes.items():
            tree.put(k,v)
        for k, v in nodes.items():
            self.assertEqual(v, tree.get(k))
        for k in [4,6,9]:
            self.assertIsNone(tree.get(k))

