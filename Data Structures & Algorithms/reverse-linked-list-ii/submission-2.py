# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return head
        if left == right:
            return head
        pos = 1
        t = head
        before = None
        while t:
            if pos<left:
                pos+=1
                before = t
                t = t.next
                continue
            break
        curr = t
        prev = None
        times = right-left+1
        while times>0:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            times-=1
        t.next = curr
        if before:
            before.next = prev
            return head
        return prev