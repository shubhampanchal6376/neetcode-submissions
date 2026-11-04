# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head: Optional[ListNode],times:int):
        curr = head
        prev = None
        while times>0:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            times-=1
        return 
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        size = 2
        left = head
        res = None
        right = left
        prevleft = None
        while True:
            right = left
            if right is None:
                break
            right = right.next
            if right:
                nextleft = right.next
                self.reverse(left,size)
                if prevleft:
                    prevleft.next = right
                prevleft = left
                if res is None:
                    res = right
                left = nextleft
            else:
                if prevleft:
                    prevleft.next = left
                if res is None:
                    res = left
                break
        return res