# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        460ms, beats: 5.62%
        """
        def in_order(root):
            if not root:
                return []
            return in_order(root.left) + [root.val] + in_order(root.right)

        vals = in_order(root)
        res = 0
        flag = False
        for i in vals:
            if flag:
                res += i
                if i == R:
                    break
            else:
                if i == L:
                    res += i
                    flag = True
        return res

    def rangeSumBST2(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        384ms, beats: 34.83%
        """
        def f(root, res=0):
            if root:
                res = f(root.left, res)
                res = f(root.right, res)
                if L <= root.val <= R:
                    res += root.val

            return res
        return f(root)
