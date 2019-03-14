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
        5.6ms, beats: 5.56%
        """
        if not root:
            return 0
        self.left_val_sum = 0
        if root.left:
            self.get_left_val(root.left, is_left=True)
        if root.right:
            self.get_left_val(root.right)
        return self.left_val_sum

    def get_left_val(self, node, is_left=False):
        if not node.left and not node.right and is_left:
            self.left_val_sum += node.val
            return
        if node.left:
            self.get_left_val(node.left, is_left=True)
        if node.right:
            self.get_left_val(node.right)

