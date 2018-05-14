# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        l = []
        if not root:
            return l
        s = str(root.val)
        if root.left:
            tmp = self.binaryTreePaths(root.left)
            for x in tmp:
                l.append(s + '->' + x)
        if root.right:
            tmp = self.binaryTreePaths(root.right)
            for x in tmp:
                l.append(s + '->' + x)
        if not root.left and not root.right:
            l.append(s)
        return l

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
a.left = b
a.right = c
b.right = d

x = Solution().binaryTreePaths(a)
print(x)