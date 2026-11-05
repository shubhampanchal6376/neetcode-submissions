# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 is None and list2 is None:
            return None
        if list1 is not None and list2 is None:
            return list1
        if list1 is None and list2 is not None:
            return list2
        head1 = list1
        head2 = list2
        head = None
        if head1.val>head2.val:
            head = head2
            head2 = head2.next
        else:
            head = head1
            head1 = head1.next
        ans = head
        while head1 and head2 :
            if head1.val>head2.val:
                head.next = head2
                head = head.next
                head2 = head2.next
            else:
                head.next = head1
                head = head.next
                head1 = head1.next
        if head1 is None and head2 is not None:
            head.next = head2
        if head2 is None and head1 is not None:
            head.next = head1
        if head1 is None and head2 is None:
            head.next = None
        return ans 