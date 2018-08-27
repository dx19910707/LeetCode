# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        40ms beats: ?
        """
        res = head
        lens = 0
        copy = head
        while copy:
            lens += 1
            copy = copy.next
        middle = lens // 2
        for i in range(1, middle + 1):
            res = res.next

        print(res.val)
        return res
