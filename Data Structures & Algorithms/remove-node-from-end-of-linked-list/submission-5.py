# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time O(n)
        # Space O(1)
        first = head
        pos = 1
    
        while pos <= n and first:
            first = first.next
            pos+=1

        if not first:
            return head.next

        second = head
        prev = head
        while first:
            first = first.next
            prev = second
            second = second.next
        
        prev.next = second.next
        return head