# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        a.sort()
        x = ListNode(a[0])
        ans = x
        for i in range(1,len(a)):
            y = ListNode(a[i])
            x.next = y
            x = x.next
        return ans