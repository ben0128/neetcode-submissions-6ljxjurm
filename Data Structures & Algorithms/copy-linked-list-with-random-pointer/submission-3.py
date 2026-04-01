"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # {[oldNode]: [newNode]}
        memo = {None: None}
        newL = dummy = Node(0)
        curr = head
        while curr:
            newNode = Node(curr.val)
            newL.next = newNode
            memo[curr] = newNode

            curr, newL = curr.next, newL.next
        
        curr = head
        newL = dummy.next

        while newL:
            newL.random = memo[curr.random]
            curr = curr.next
            newL = newL.next

        return dummy.next
