# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        28ms
        """
        if not root:
            return False
        current_level = [root]
        level_val_list = [[root.val]]
        while current_level:
            next_level = []
            tmp = []
            for current_root in current_level:
                if current_root.left:
                    next_level.append(current_root.left)
                    tmp.append(current_root.left.val)
                else:
                    tmp.append(None)
                if current_root.right:
                    next_level.append(current_root.right)
                    tmp.append(current_root.right.val)
                else:
                    tmp.append(None)
            current_level = next_level
            level_val_list.append(tmp)

        for level in level_val_list:
            if (x in level and y not in level) or (x not in level and y in level):
                return False
            if x in level and y in level:
                x_index = level.index(x)
                y_index = level.index(y)
                x_index, y_index = min(x_index, y_index), max(x_index, y_index)
                if y_index - x_index == 1 and x_index % 2 == 0:
                    return False
                else:
                    return True
        return False
