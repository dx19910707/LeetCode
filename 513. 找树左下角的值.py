# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur_level = [root]
        res = None
        while cur_level:
            res = cur_level[0].val
            next_level = []
            for cur_root in cur_level:
                if cur_root.left:
                    next_level.append(cur_root.left)
                if cur_root.right:
                    next_level.append(cur_root.right)
            cur_level = next_level
        return res