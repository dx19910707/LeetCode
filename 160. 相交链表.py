# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        252ms beats: 94.34%
        """
        d = set()
        tmp = headA
        while tmp:
            d.add(tmp)
            tmp = tmp.next
        tmp = headB
        while tmp:
            if tmp in d:
                return tmp
            tmp = tmp.next
        return None
