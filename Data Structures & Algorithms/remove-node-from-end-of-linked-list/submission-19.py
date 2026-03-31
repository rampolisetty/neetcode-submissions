# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = head
        right = dummy # starts one step BEHIND head

        for _ in range(n):
            left = left.next
        
        while left:
            left = left.next
            right = right.next
        
        # right lands exactly on the predecessor of the node to remove 
        right.next = right.next.next # Delete

        return dummy.next # Head
