# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        72ms beats:99.74%
        今天心情不好，状态差，代码丑，不想改了
        """
        flag = 0
        copy = l1
        while True:
            if l1 and l2:
                s = l1.val + l2.val + flag
                if s >= 10:
                    s -= 10
                    flag = 1
                else:
                    flag = 0
                l1.val = s
            if not l1.next:
                last_node = l1
                l1.next = l2.next
                l1 = l1.next
                break
            elif not l2.next:
                last_node = l1
                l1 = l1.next
                break
            l1 = l1.next
            l2 = l2.next
        while flag:
            if l1:
                s = l1.val + 1
                if s >= 10:
                    s -= 10
                    flag = 1
                else:
                    flag = 0
                l1.val = s
                last_node = l1
                l1 = l1.next
            else:
                last_node.next = ListNode(1)
                flag = 0
        return copy
