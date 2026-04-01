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
        hashMap = {}
        dup = Node(0)
        ans = dup
        curr = head
        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            new_Node = hashMap[curr]
            ans.next = new_Node
            if curr.random != None:    
                ans.next.random = hashMap[curr.random]
            else:
                ans.next.random = None
            ans = ans.next
            curr = curr.next
        return dup.next