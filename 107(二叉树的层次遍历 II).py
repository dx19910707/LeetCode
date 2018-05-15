# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        cur_level = [root]
        while cur_level:
            next_level = []
            l = []
            for cur_root in cur_level:
                l.append(cur_root.val)
                if cur_root.left:
                    next_level.append(cur_root.left)
                if cur_root.right:
                    next_level.append(cur_root.right)
            cur_level = next_level
            res.append(l)
        return res[::-1]
