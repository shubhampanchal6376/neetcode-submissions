# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr is None:
            return head
        p = ListNode(head.val)
        ans = p
        while curr.next:
            curr = curr.next
            if curr.val == p.val:
                continue
            else:
                q = ListNode(curr.val)
                p.next = q
                p = q
        return ans