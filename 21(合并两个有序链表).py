# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        将两个链表的所有的值取出来排序后构建新的链表
        """
        def get_nums(listnode):
            nums = []
            if listnode:
                nums.append(listnode.val)
                while listnode.next:
                    nums.append(listnode.next.val)
                    listnode = listnode.next
            return nums
        nums1 = get_nums(l1)
        nums2 = get_nums(l2)
        nums = nums1 + nums2
        if not nums:
            return
        nums.sort()
        res = tmp = None
        for i in nums:
            if isinstance(tmp,ListNode):
                tmp.next = ListNode(i)
                tmp = tmp.next
            else:
                tmp = ListNode(i)
                res = tmp
        return res
