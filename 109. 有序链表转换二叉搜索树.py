# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        def make_node(l):
            if not l:
                return None
            middle = len(l) // 2
            node = TreeNode(l[middle])
            node.left = make_node(l[:middle])
            if middle < len(l)-1:
                node.right = make_node(l[middle+1:])
            else:
                node.right = None
            return node
        node = make_node(l)
        return node