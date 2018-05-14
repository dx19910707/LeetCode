# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return
        if t1 is not None and t2 is not None:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
            return t1
        return t1 or t2

a1 = TreeNode(1)
b1 = TreeNode(3)
c1 = TreeNode(2)
d1 = TreeNode(5)
a1.left = b1
a1.right = c1
b1.left = d1

a2 = TreeNode(2)
b2 = TreeNode(1)
c2 = TreeNode(3)
d2 = TreeNode(4)
e2 = TreeNode(7)
a2.left = b2
a2.right = c2
b2.right = d2
c2.right = e2
Solution().mergeTrees(a1,a2)