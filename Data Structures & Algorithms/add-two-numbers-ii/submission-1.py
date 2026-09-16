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
        x = 0 
        y = 0 
        for i in a:
            x = x*10 + i
        for i in b:
            y = y*10 + i
        c = x+y
        l = []
        if c == 0 :
            return ListNode(0)
        while c>0:
            temp = c%10
            l.append(temp)
            c = c//10
        l = l[::-1]
        t = ListNode(l[0]) 
        ans = t
        for i in range(1,len(l)):
            f = ListNode(l[i])
            t.next = f
            t = f
        return ans















