# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cur_level = [root]
        l = []
        while cur_level:
            next_level = []
            for cur_root in cur_level:
                l.append(cur_root.val)
                if cur_root.left:
                    next_level.append(cur_root.left)
                if cur_root.right:
                    next_level.append(cur_root.right)
            cur_level = next_level
        l.sort()
        return l[k-1]