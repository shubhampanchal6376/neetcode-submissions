# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next
        b = a[::-1]
        l = ListNode(b[0])
        w = l
        for i in range(1,len(b)):
            t = ListNode(b[i])
            w.next = t
            w = t
        return l