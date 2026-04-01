# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None)
        ans = head
        if not list1 and not list2:
            return None
        while list1 and list2:
            if list1.val > list2.val:
                head.val = list2.val
                list2 = list2.next
            else:
                head.val = list1.val
                list1 = list1.next

            head.next = ListNode()
            head = head.next
        print('check', ans.val)
        if not list1 and list2:
            head.val = list2.val
            head.next = list2.next
        if not list2 and list1:
            head.val = list1.val
            head.next = list1.next

        return ans