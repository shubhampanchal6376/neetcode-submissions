# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while list1 is not None:
            x = list1.val
            ans.append(x)
            list1 = list1.next
        while list2 is not None:
            x = list2.val
            ans.append(x)
            list2 = list2.next
        ans.sort()
        temp = ListNode(0)
        curr = temp
        for i in ans:
            curr.next = ListNode(i)
            curr = curr.next 
        return temp.next