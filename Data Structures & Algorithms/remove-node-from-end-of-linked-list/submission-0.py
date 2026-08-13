# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        curr = head
        while curr:
            c+=1
            curr = curr.next
        x = c-n
        curr = head
        while x>1:
            curr = curr.next
            x-=1
        if x == 0 and n == 1:
            return head.next
        elif x == 0 and n != 1:
            curr = curr.next
            head = curr
        else:
            curr.next = curr.next.next
        return head