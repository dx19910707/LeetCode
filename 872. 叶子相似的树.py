# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        52ms beats: 无图表
        """
        val1 = []

        def get_val1(root):
            if root.left is None and root.right is None:
                val1.append(root.val)
            if root.left:
                get_val1(root.left)
            if root.right:
                get_val1(root.right)

        def judge(root):
            if not root.left and not root.right:
                if root.val == val1[0]:
                    val1.pop(0)
                else:
                    return False
            if root.left:
                judge(root.left)
            if root.right:
                judge(root.right)
            if val1:
                return False
            return True

        if not root1 or not root2:
            return False

        get_val1(root1)
        return judge(root2)
