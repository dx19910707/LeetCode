# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        t = 1
        l = []
        dummy = ListNode('dummy')
        node = dummy
        while head:
            if m <= t <= n:
                l.append(head)
            elif t < m:
                node.next = head
                node = node.next
            else:
                break
            t += 1
            head = head.next
        for tmp in l[::-1]:
            node.next = tmp
            node = node.next
        node.next = head
        return dummy.next
