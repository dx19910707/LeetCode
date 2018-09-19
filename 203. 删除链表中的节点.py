# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        80ms beats: 84.12%
        """
        while head and head.val == val:
            head = head.next
        last = now = head
        while now:
            if now.val == val:
                now = now.next
                last.next = now
            else:
                last, now = now, now.next
        return head
