# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode | None , times : int):
        curr = head
        prev = None
        while times>0:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            times-=1
        return
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if head == None:
            return head
        size = k
        left = head
        res = None
        prevleft = None
        right = left
        while True:
            right = left
            for i in range(k-1):
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