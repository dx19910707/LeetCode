# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        def get_val(root):
            if not root:
                return []
            return get_val(root.left) + [root.val] + get_val(root.right)
        def get_root(root):
            if not root:
                return []
            return get_root(root.left) + [root] + get_root(root.right)
        val_list = get_val(root)[::-1]
        root_list = get_root(root)
        # leetcode itertools.accumulate不可用
        tmp = 0
        for i in range(len(val_list)):
            val_list[i] += tmp
            tmp = val_list[i]
        accu_val_list = val_list[::-1]
        for i in range(len(root_list)):
            root_list[i].val = accu_val_list[i]
        return root