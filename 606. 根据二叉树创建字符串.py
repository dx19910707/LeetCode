# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        56ms, beats: 60.69%
        """
        if not t:
            return ''
        res = str(t.val)
        has_left = False
        if t.left:
            res += '({})'.format(self.tree2str(t.left))
            has_left = True
        if t.right:
            if not has_left:
                res += '()'
            res += '({})'.format(self.tree2str(t.right))
        return res
