# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        124ms, beats: 35.44%
        """
        def middle_sort(root):
            if not root:
                return []
            return middle_sort(root.left) + [root.val] + middle_sort(root.right)

        value_list = middle_sort(root)
        node = head = TreeNode(value_list[0])
        for i in value_list[1:]:
            node.right = TreeNode(i)
            node = node.right

        return head
