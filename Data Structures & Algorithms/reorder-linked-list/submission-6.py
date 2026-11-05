class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        slow = head
        fast = head

        # Find middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Separate second half
        curr = slow.next
        slow.next = None

        # Reverse second half
        prev = None
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        ans = head
        curr = head

        # Merge
        while head and prev:

            temp1 = head.next
            temp2 = prev.next

            curr.next = prev
            prev.next = temp1

            curr = temp1

            head = temp1
            prev = temp2

        return None