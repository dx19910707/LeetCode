# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        56ms, beats: 99%
        """
        seen = set()
        while head:
            if head in seen:
                return head
            else:
                seen.add(head)
            head = head.next
        return None

    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        84ms, beats: 11.77%
        """
        slow = fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        if has_cycle:
            new_slow = head
            while slow != new_slow:
                slow = slow.next
                new_slow = new_slow.next
            return new_slow
        return None
