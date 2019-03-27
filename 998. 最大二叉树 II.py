# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        44ms
        """
        node_list = self.in_order(root)
        node_list.append(TreeNode(val))
        return self.helper(node_list)

    def in_order(self, root):
        if not root:
            return []
        return self.in_order(root.left) + [root] + self.in_order(root.right)

    def helper(self, l):
        stack = []
        for node in l:
            while stack and node.val > stack[-1].val:
                node.left = stack.pop()
            if stack and node.val < stack[-1].val:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

    def insertIntoMaxTree2(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        40ms
        """
        t = TreeNode(val)
        if not root:
            return t
        if val > root.val:
            t.left = root
            return t
        self.helper2(root, root.right, t)
        return root

    def helper2(self, pre_node, cur_node, insert_node):
        if not cur_node:
            pre_node.right = insert_node
        elif insert_node.val > cur_node.val:
            insert_node.left = cur_node
            pre_node.right = insert_node
        else:
            self.helper2(cur_node, cur_node.right, insert_node)
