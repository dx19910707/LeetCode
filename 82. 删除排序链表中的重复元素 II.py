# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        60ms, beats:7.67%
        """
        if not head:
            return None
        pre_node = head
        head = head.next
        count = 1
        l = []
        while head:
            if head.val != pre_node.val:
                if count == 1:
                    l.append(pre_node)
                else:
                    count = 1
                pre_node = head
            else:
                count += 1
            head = head.next
        if count == 1:
            l.append(pre_node)
        if not l:
            return None
        root = l[0]
        node = root
        for i in l[1:]:
            node.next = i
            node = i
        node.next = None
        return root
