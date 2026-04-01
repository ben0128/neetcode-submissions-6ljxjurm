# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow - fast pointer
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev

            prev, second = second, nxt

        h1, h2 = head, prev
        while h1 and h2:
            nt1, nt2 = h1.next, h2.next
            h1.next, h2.next = h2, nt1

            h1, h2 = nt1, nt2