# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        76ms
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        right_start_index = len(preorder)
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                right_start_index = i
                break
        root.left = self.bstFromPreorder(preorder[1:right_start_index])
        root.right = self.bstFromPreorder(preorder[right_start_index:])
        return root
