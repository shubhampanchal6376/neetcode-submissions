# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        b = []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        n = 0
        for i in a[::-1]:
            n = n*10+i
        m = 0
        for j in b[::-1]:
            m = m*10 + j
        g = n+m
        l = ListNode(g%10)
        w = l
        g//=10
        while g > 0 :
            t = ListNode(g%10)
            w.next = t
            w = t
            g//=10
        return l
