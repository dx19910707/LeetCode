# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        def get_val(root):
            if not root:
                return []
            return get_val(root.left) + [root.val] + get_val(root.right)
        l = get_val(root)
        l.sort()
        m = l[0]
        for i in l:
            if i > m:
                return i
        return -1