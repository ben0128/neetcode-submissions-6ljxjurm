# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # sc = O(N), tc = O(N)
        # method 1:
        # numSet = set()
        # while ....:
            # return False

        # return True
        
        #  sc = O(1), tc = O(N)
        #  method 2: slow fast pointer
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        return False