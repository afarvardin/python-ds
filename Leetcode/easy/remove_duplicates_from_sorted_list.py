from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
node6 = ListNode(4)


# Link the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

cls = Solution()

node = cls.deleteDuplicates(node1)

while node:
    print(node.val, end=" -> ")
    node = node.next
print('None')