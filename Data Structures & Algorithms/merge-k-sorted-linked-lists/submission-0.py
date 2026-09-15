# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        a = []
        for i in lists:
            while i:
                a.append(i.val)
                i = i.next
        a.sort()
        if len(a)==0:
            return None
        x = ListNode(a[0])
        y = x
        for i in range(1,len(a)):
            c = ListNode(a[i])
            y.next = c
            y = c
        return x