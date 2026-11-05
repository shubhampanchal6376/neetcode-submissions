class Node:
    def __init__(self,val = 0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        for _ in range(index):
            if not curr:
                return -1
            curr = curr.next
        if not curr:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index ==0:
            self.addAtHead(val)
            return 
        curr = self.head
        for _ in range(index-1):
            if not curr:
                return 
            curr = curr.next
        if not curr:
            return 
        node = Node(val)
        node.next = curr.next
        curr.next = node

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return 
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        for _ in range(index-1):
            if not curr.next:
                return 
            curr = curr.next
        if not curr.next:
            return 
        curr.next = curr.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)