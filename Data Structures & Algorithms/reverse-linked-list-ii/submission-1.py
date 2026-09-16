# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        a = []
        curr = head
        if left == right:
            return head
        while curr:
            a.append(curr.val)
            curr = curr.next
        ans = []
        for i in range(left-1,right):
            ans.append(a[i])
        t = ans[::-1]
        m = a[:left-1] + t + a[right:]
        g = ListNode(m[0])
        y = g
        for i in range(1,len(m)):
            h = ListNode(m[i])
            g.next = h
            g = h
        return y