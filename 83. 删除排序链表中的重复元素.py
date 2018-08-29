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
        40ms beats: 99.68%
        """
        if head is None or head.next is None:
            return head
        if head.val == head.next.val:
            head.next = head.next.next
            head = Solution().deleteDuplicates(head)
        else:
            head.next = Solution().deleteDuplicates(head.next)
        return head
