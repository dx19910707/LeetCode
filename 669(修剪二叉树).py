# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val < L:
            return self.trimBST(root.right,L,R)
        if root.val > R:
            return self.trimBST(root.left,L,R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

a1 = TreeNode(3)
a2 = TreeNode(0)
a3 = TreeNode(4)
a4 = TreeNode(2)
a5 = TreeNode(1)
a1.left = a2
a1.right = a3
a2.right = a4
a4.left = a5
L = 1
R = 3
x = Solution().trimBST(a1,L,R)
print(x)
