# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        middle = len(nums) // 2
        tree = TreeNode(nums[middle])
        left = nums[:middle]
        right = nums[middle + 1:]
        tree.left = self.sortedArrayToBST(left)
        tree.right = self.sortedArrayToBST(right)
        return tree
