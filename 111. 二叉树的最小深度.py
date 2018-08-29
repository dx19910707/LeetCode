# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        40ms beats: 100%
        """
        if not root:
            return 0
        current_level = [root]
        i = 0
        while current_level:
            i += 1
            next_level = []
            for current_root in current_level:
                if not current_root.left and not current_root.right:
                    return i
                if current_root.left:
                    next_level.append(current_root.left)
                if current_root.right:
                    next_level.append(current_root.right)
            current_level = next_level
        return i
