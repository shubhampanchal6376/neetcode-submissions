# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = None
        temp = head
        front = temp.next
        while temp:
            temp.next = prev
            prev = temp
            temp = front
            if temp == None:
                return prev
            front = front.next
