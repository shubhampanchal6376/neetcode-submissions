# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next
        b = []
        l = 0 
        r = len(a)-1
        while l<=r:
            if l == r:
                b.append(a[l])
            else:
                b.append(a[l])
                b.append(a[r])
            l+=1
            r-=1
        t = head
        i = 0
        while head:
            head.val = b[i]
            head = head.next
            i+=1
        














