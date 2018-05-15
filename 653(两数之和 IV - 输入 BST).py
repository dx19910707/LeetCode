# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        def get_val(root):
            if not root:
                return []
            return get_val(root.left) + [root.val] + get_val(root.right)

        res = get_val(root)
        d = {}
        for i in res:
            if k - i in d:
                return True
            d[i] = k - i
        return False

