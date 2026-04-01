# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev, nxt = None, head.next
        while nxt:
            head.next = prev
            prev = head
            head = nxt
            nxt = head.next
        head.next = prev
        return head 
        # step 1: nxt = head.next
        # step 2: head.next = prev
        # step 3: prev = head
        # step 4: head = nxt
        