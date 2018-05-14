# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        比较两棵树转换成列表后是否相同
        """
        def trans(node):
            if not node:
                return [None]
            l = [node.val] + trans(node.left) + trans(node.right)
            return l
        return trans(p) == trans(q)

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(1)
a1.left = a2
a1.right = a3

b1 = TreeNode(1)
b2 = TreeNode(1)
b3 = TreeNode(2)
b1.left = b2
b1.right = b3

print(Solution().isSameTree(a1,b1))