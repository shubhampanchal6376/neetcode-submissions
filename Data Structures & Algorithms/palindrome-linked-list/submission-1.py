# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        # bring slow at the middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # initialize prev with None and remove LL from the slow node 
        prev = None
        while slow:
            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex
        # start compairing with the very last node of the reversed part means prev :: it is liek compairng the last(prev) with the first(head) elements in an array 
        while prev:
            if head.val!=prev.val:
                return False
            head = head.next
            prev = prev.next
        return True