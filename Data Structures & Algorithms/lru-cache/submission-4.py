class Node:
    def __init__(self, val, key):
        self.value, self.key = val, key
        self.prev = self.nxt = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.memo = {}
        self.dummy_head = Node(-1, -1)
        self.dummy_tail = Node(-1, -1)
        self.dummy_head.nxt = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
    
    def get(self, key: int) -> int:
        if key not in self.memo:
            return -1
        
        n = self.memo[key]
        self.removeSelfNode(n)
        self.moveNodeToHead(n)
        
        return n.value
    
    def removeSelfNode(self, n):
        prev, nxt = n.prev, n.nxt
        prev.nxt, nxt.prev = nxt, prev
        n.prev = n.nxt = None
    
    def moveNodeToHead(self, n):
        n.prev, n.nxt = self.dummy_head, self.dummy_head.nxt
        nxt = self.dummy_head.nxt
        nxt.prev = self.dummy_head.nxt = n
        
        
    def put(self, key: int, value: int) -> None:
        # node is already exist 
        if key in self.memo:
            n = self.memo[key]
            n.value = value
            self.removeSelfNode(n)
            self.moveNodeToHead(n)
            return
        
        if self.cap == len(self.memo):
            tailNode = self.dummy_tail.prev
            del self.memo[tailNode.key]
            self.removeSelfNode(tailNode)
            # need to add new node
        
        new_node = Node(value, key)
        self.memo[key] = new_node
        self.moveNodeToHead(new_node)
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)