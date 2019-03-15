# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        60ms, beats: 91.36%
        """
        self.sum = 0
        self._findtilt(root, 0)
        return self.sum

    def _findtilt(self, node, res):
        if not node:
            return 0
        ls = self._findtilt(node.left, res)
        rs = self._findtilt(node.right, res)
        self.sum += abs(ls - rs)
        return node.val + ls + rs
