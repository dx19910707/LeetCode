# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        140ms, beats 66.67%
        """
        count = 0
        node = head
        flag = False
        G = set(G)
        while node:
            if node.val in G:
                flag = True
            else:
                if flag:
                    count += 1
                flag = False
            node = node.next
        count += 1 if flag else 0
        return count


l = ListNode
a1 = l(0)
a2 = l(1)
a3 = l(2)
a4 = l(3)
a5 = l(4)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
g = [0, 3, 1, 4]
s = Solution()
r = s.numComponents(a1, g)
print(r)
