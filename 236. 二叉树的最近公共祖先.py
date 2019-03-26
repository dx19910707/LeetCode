# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        in_order_list = self.in_order(root)
        p_index = in_order_list.index(p)
        q_index = in_order_list.index(q)
        if p_index > q_index:
            p_index, q_index = q_index, p_index
        while True:
            root_index = in_order_list.index(root)
            if p_index <= root_index <= q_index:
                return root
            elif root_index > q_index:
                root = root.left
            else:
                root = root.right

    def in_order(self, root):
        if not root:
            return []
        return self.in_order(root.left) + [root] + self.in_order(root.right)
