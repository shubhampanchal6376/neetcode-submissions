# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        n = 1
        while curr.next:
            n+=1
            curr = curr.next
        k = k%n
        if k==0:
            return head
        t = n-k
        temp = head
        while t>1:
            temp=temp.next
            t-=1
        curr.next = head
        head = temp.next
        temp.next = None
        return head
