# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode(None)

        minH = []
        for idx, list in enumerate(lists):
            if list:
                heapq.heappush(minH, (list.val, idx, list))
        
        while minH:
            _, i, n = heapq.heappop(minH)
            
            head.next = n
            head = head.next 
            n = n.next
            if n:
                heapq.heappush(minH, (n.val, i, n))
            
        return dummy.next
