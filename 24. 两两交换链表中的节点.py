# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        n = 1
        def change_head(pre_head,cur_head,n):
            if not cur_head.next:
                if n % 2 == 0:
                    cur_head.next = pre_head
                    pre_head.next = None
                return cur_head
            if n % 2 ==0:
                tmp = cur_head.next
                cur_head.next = pre_head
                pre_head.next = change_head(pre_head,tmp,n+1)
                return cur_head
            else:
                return change_head(cur_head,cur_head.next,n+1)

        if not head.next:
            return head
        res = change_head(head,head.next,n+1)
        return res