# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next
        n = len(a)
        m = float('-inf')
        for i in range(len(a)):
            x = a[i]
            y = a[n-i-1]
            if n-i-1<0:
                break
            if m<x+y:
                m = x+y
        return m