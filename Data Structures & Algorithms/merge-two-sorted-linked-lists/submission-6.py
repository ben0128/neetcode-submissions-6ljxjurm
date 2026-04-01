# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                head.next = h1
                h1 = h1.next
            else:
                head.next = h2
                h2 = h2.next
            head = head.next
            
        if h1:
            head.next = h1
        elif h2:
            head.next = h2
        
        return dummy.next
