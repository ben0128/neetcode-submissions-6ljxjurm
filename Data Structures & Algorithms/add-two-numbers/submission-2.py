# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 => 2 => 3
        # 3 => 4 => 5
    # res:4 => 6 => 8

        # 1 => 7 => 3        371+643 = 1014
        # 3 => 4 => 6
    # res:4 => 1 => 0 => 1    

        # 0
        # 0
    # res:0

        # 9 => 9 => 9 => 9 => 9 => 9
        # 9 => 9 => 9 => 9 => 9 => 9

        # step 1: init isAddOne: bool
        isAddOne = False
        curr = dummy = ListNode()
        while l1 or l2:
            val1, val2 = l1.val if l1 != None else 0, l2.val if l2 != None else 0
            currSum = val1 + val2 + (1 if isAddOne else 0)
            isAddOne = False
            if currSum >= 10:
                currSum -= 10
                isAddOne = True
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            curr.next = ListNode(currSum)
            curr = curr.next
        
        if isAddOne:
            curr.next = ListNode(1)

        return dummy.next
