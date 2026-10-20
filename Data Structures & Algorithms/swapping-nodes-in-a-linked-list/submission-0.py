# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []
        curr = head
        while head:
            a.append(head.val)
            head = head.next 
        a[k-1], a[-k] = a[-k], a[k-1]
        p = ListNode(a[0])
        ans = p
        for i in range(1,len(a)):
            t = ListNode(a[i])
            p.next = t
            p = p.next
        return ans