# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        452ms, beats: 53.55%
        """
        if not head:
            return None
        new_head = tail = head
        head = head.next
        while head:
            tmp = new_head
            if head.val < tmp.val:
                tail.next = head.next
                head.next = tmp
                new_head = head
                head = tail.next
            elif tmp.val <= head.val < tail.val:
                tail.next = head.next
                while tmp:
                    if tmp.val <= head.val < tmp.next.val:
                        head.next = tmp.next
                        tmp.next = head
                        head = tail.next
                        break
                    tmp = tmp.next
            else:
                tail = head
                head = head.next
        return new_head
