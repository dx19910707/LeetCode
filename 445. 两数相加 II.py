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
        """
        if not l1:
            return l2
        if not l2:
            return l1
        list1 = []
        list2 = []
        tmp1 = l1
        tmp2 = l2
        while tmp1:
            list1.insert(0,tmp1.val)
            tmp1  = tmp1.next
        while tmp2:
            list2.insert(0,tmp2.val)
            tmp2 = tmp2.next
        def change(l,list):
            if not l:
                return
            l.val = list.pop()
            change(l.next,list)
        add = 0
        i = 0
        if len(list1) >= len(list2):
            while i < len(list2):
                list1[i] = list1[i] + list2[i] + add
                if list1[i] >= 10:
                    list1[i] -= 10
                    add = 1
                else:
                    add = 0
                i += 1
            if add == 1:
                while i < len(list1):
                    list1[i] += add
                    if list1[i] >= 10:
                        list1[i] -= 10
                        add = 1
                        i += 1
                    else:
                        add = 0
                        break
            change(l1,list1)
            if add == 1:
                add_list = ListNode(1)
                add_list.next = l1
                return add_list
            return l1
        else:
            while i < len(list1):
                list2[i] = list1[i] + list2[i] + add
                if list2[i] >= 10:
                    list2[i] -= 10
                    add = 1
                else:
                    add = 0
                i += 1
            if add == 1:
                while i < len(list2):
                    list2[i] += add
                    if list2[i] >= 10:
                        list2[i] -= 10
                        add = 1
                        i += 1
                    else:
                        add = 0
                        break
            change(l2,list2)
            if add == 1:
                add_list = ListNode(1)
                add_list.next = l2
                return add_list
            return l2
