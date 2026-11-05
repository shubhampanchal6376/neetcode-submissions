# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = head
        while prev and prev.val in nums:
            head = head.next
            prev = head
        if prev is None:
            return prev
        ans = prev
        curr = prev
        while curr:
            if curr.val in nums:
                prev.next = prev.next.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return ans