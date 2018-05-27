# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        cur_level = [root]
        res = []
        while cur_level:
            next_level = []
            m = []
            for cur_root in cur_level:
                m.append(cur_root.val)
                if cur_root.left:
                    next_level.append(cur_root.left)
                if cur_root.right:
                    next_level.append(cur_root.right)
            cur_level = next_level
            res.append(max(m))
        return res