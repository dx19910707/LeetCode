class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        vals = []
        while tmp:
            vals.append(tmp.val)
            tmp = tmp.next
        def reverse(head,vals):
            if not head:
                return
            head.val = vals.pop()
            reverse(head.next,vals)
        reverse(head,vals)
        return head

    def reverseList2(self, head):
        new_head = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head