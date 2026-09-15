# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next
        ans = []
        temp = []
        for i in a:
            temp.append(i)
            if len(temp)==k:
                ans = ans + temp[::-1]
                temp.clear()
        ans = ans+temp
        x = ListNode(ans[0])
        n = x
        for i in range(1,len(ans)):
            y = ListNode(ans[i])
            n.next = y
            n = y
        return x