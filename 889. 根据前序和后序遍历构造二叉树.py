# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        72ms
        """
        if not pre and not post:
            return None
        root = TreeNode(pre[0])
        left = 1
        right = -2
        node = root
        while left < len(pre) and pre[left] == post[right]:
            node.left = TreeNode(pre[left])
            node = node.left
            left += 1
            right -= 1
        pre = pre[left:]
        post = post[:right+1]
        if pre:
            index1 = pre.index(post[-1])
            index2 = post.index(pre[0])
            node.left = self.constructFromPrePost(pre[:index1], post[:index2+1])
            node.right = self.constructFromPrePost(pre[index1:], post[index2+1:])
        return root
