# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        def getsum(root,pre):
            if not root.left and not root.right:
                self.res += pre * 10 + root.val
            if root.left:
                getsum(root.left,pre*10+root.val)
            if root.right:
                getsum(root.right,pre*10+root.val)
        getsum(root,pre=0)
        return self.res