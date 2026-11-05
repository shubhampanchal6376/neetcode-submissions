# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if head is None:
            return head
        prev = head
        while prev and prev.val == val:
            head = head.next
            prev = head
        if prev is None:
            return prev
        ans = prev
        curr = prev.next
        while curr:
            if curr.val==val:
                prev.next = prev.next.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return ans