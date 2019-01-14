# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        root_value = root.val
        current_level = [root]
        while current_level:
            next_level = []
            for current_root in current_level:
                if current_root.val != root_value:
                    return False
                if current_root.left:
                    next_level.append(current_root.left)
                if current_root.right:
                    next_level.append(current_root.right)
            current_level = next_level
        return True
