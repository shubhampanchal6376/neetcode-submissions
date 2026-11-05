# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        head = list1
        if head is None:
            return head
        curr = head
        A = None
        B = None
        C = None
        while a>1:
            curr = curr.next
            a-=1
        A = curr
        curr = head
        while b>0:
            curr = curr.next
            b-=1
        B = curr.next
        C = list2
        while C.next:
            C = C.next
        A.next = list2
        C.next = B
        return head