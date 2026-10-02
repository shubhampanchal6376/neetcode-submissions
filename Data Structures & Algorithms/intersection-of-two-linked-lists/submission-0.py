# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = []
        b = []

        curr = headA
        while curr:
            a.append(curr)
            curr = curr.next

        curr = headB
        while curr:
            b.append(curr)
            curr = curr.next

        i = len(a) - 1
        j = len(b) - 1
        ans = None

        while i >= 0 and j >= 0 and a[i] is b[j]:
            ans = a[i]
            i -= 1
            j -= 1

        return ans
        