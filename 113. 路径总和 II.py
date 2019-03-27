# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        64ms
        """
        self.res = []
        if root:
            self.helper(root, sum, [])
        return self.res

    def helper(self, root, sum, l):
        if root.left:
            self.helper(root.left, sum - root.val, l + [root.val])
        if root.right:
            self.helper(root.right, sum - root.val, l + [root.val])
        if not root.left and not root.right and root.val == sum:
            self.res.append(l + [root.val])
