# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root

a1 = TreeNode(4)
b1 = TreeNode(2)
c1 = TreeNode(7)
d1 = TreeNode(1)
e1 = TreeNode(3)
f1 = TreeNode(6)
g1 = TreeNode(9)
a1.left = b1
a1.right = c1
b1.left = d1
b1.right = e1
c1.left = f1
c1.right = g1

Solution().invertTree(a1)
