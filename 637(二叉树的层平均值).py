# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        l = []
        if not root:
            return l
        current_level = [root]
        while current_level:
            next_level = []
            level_sum = 0
            for current_root in current_level:
                level_sum += current_root.val
                if current_root.left:
                    next_level.append(current_root.left)
                if current_root.right:
                    next_level.append(current_root.right)
            l.append(level_sum / float(len(current_level)))
            current_level = next_level
        return l

a1 = TreeNode(3)
a2 = TreeNode(9)
a3 = TreeNode(20)
a4 = TreeNode(15)
a5 = TreeNode(7)
a1.left = a2
a1.right = a3
a3.left = a4
a3.right = a5
x = Solution().averageOfLevels(a1)
print(x)