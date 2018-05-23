# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        if not root:
            return l
        cur_level = [root]
        while cur_level:
            next_level = []
            l.append(cur_level[-1].val)
            for cur_root in cur_level:
                if cur_root.left:
                    next_level.append(cur_root.left)
                if cur_root.right:
                    next_level.append(cur_root.right)
            cur_level = next_level
        return l