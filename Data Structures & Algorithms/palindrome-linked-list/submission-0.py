# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        ans = []
        while curr:
            a = curr.val
            ans.append(a)
            curr = curr.next
        return ans == ans[::-1]