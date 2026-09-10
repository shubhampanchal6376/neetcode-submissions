# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = []
        curr = head
        if head is None:
            return head
        while curr:
            ans.append(curr.val)
            curr = curr.next
        n = len(ans)
        if n==1:
            return head
        k = k%n
        while k>0:
            a = ans[-1]
            ans = [a] + ans
            ans.pop()
            k-=1
        p = ListNode(ans[0])

        a = p
        for i in range(1,len(ans)):
            x = ListNode(ans[i])
            a.next = x
            a = x
        return p