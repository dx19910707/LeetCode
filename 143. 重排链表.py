# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        tmp = head
        l = []
        while tmp.next:
            l.append(tmp.next)
            tmp = tmp.next
        t = 0
        while t < len(l):
            head.next = l.pop()
            head = head.next
            if t < len(l):
                head.next = l[t]
                head = head.next
                t += 1
            else:
                break
        head.next = None
