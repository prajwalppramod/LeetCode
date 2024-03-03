# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        ptr2 = head
        count = 0  # Start count from 0

        while ptr is not None:
            ptr = ptr.next
            count += 1

        # For even number of nodes, ptr2 will stop at the first middle node
        for i in range(count // 2):
            ptr2 = ptr2.next

        return ptr2



        