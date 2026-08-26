# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next
        b = []
        for i in a:
            if i != val:
                b.append(i)
        if len(b)==0:
            return None
        g = ListNode(b[0])
        x = g
        for i in range(1,len(b)):
            c = ListNode(b[i])
            x.next = c
            x = x.next
        head = g
        return g