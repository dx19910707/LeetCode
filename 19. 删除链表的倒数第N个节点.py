# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def delete(cur_node, next_node, _n):
            if not next_node:
                return 0
            _next = next_node.next
            a = delete(next_node, _next, _n) + 1
            if a == _n:
                cur_node.next = _next
            return a

        if not head:
            return head
        head_index = delete(head, head.next, n) + 1
        if head_index == n:
            return head.next
        return head


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

s = Solution()
r = s.removeNthFromEnd(a1, 1)
