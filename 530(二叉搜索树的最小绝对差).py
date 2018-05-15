# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        通过中序遍历获得每个节点的值
        """
        def get_val(root):
            if not root:
                return []
            return get_val(root.left) + [root.val] + get_val(root.right)

        l = get_val(root.left) + [root.val] +get_val(root.right)
        return min([abs(l[i]-l[i+1]) for i in range(len(l)-1)])

a1 = TreeNode(0)
a2 = TreeNode(2236)
a3 = TreeNode(1277)
a4 = TreeNode(2776)
a5 = TreeNode(519)
a1.right = a2
a2.left = a3
a2.right = a4
a3.left = a5

x = Solution().getMinimumDifference(a1)
print(x)