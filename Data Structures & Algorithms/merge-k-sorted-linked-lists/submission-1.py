# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        tmp = [(el.val, i) for i, el in enumerate(lists) if el]
        dummy = head = ListNode(None)
        heapq.heapify(tmp)
        
        while tmp:
            v, j = heapq.heappop(tmp)
            dummy.next = lists[j]
            dummy = dummy.next
            lists[j] = lists[j].next
            if lists[j]:
                heapq.heappush(tmp, (lists[j].val, j))
        return head.next