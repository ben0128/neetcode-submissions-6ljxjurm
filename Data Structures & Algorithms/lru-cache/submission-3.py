class LRUCache:
    # ListNode():
    def createNode(self, value, key):
        return { "val": value, "key": key, "prev": None, "nxt": None}
    def __init__(self, capacity: int):
        self.cap = capacity
        self.memo = {}
        self.dummy_head = self.createNode(-1, -1)
        self.dummy_tail = self.createNode(-1, -1)
        self.dummy_head["nxt"] = self.dummy_tail
        self.dummy_tail["prev"] = self.dummy_head
    
    def get(self, key: int) -> int:
        if key not in self.memo:
            return -1
        
        n = self.memo[key]
        self.removeSelfNode(n)
        self.moveNodeToHead(n)
        
        return n["val"]
    
    def removeSelfNode(self, n):
        prev, nxt = n["prev"], n["nxt"]
        prev["nxt"], nxt["prev"] = nxt, prev
        n["prev"] = n["nxt"] = None
    
    def moveNodeToHead(self, n):
        n["prev"], n["nxt"] = self.dummy_head, self.dummy_head["nxt"]
        self.dummy_head["nxt"]["prev"] = n
        self.dummy_head["nxt"] = n
        
        
    def put(self, key: int, value: int) -> None:
        print(key, value)
        # node is already exist 
        if key in self.memo:
            n = self.memo[key]
            n["val"] = value
            self.removeSelfNode(n)
            self.moveNodeToHead(n)
            return
        
        if self.cap == len(self.memo):
            tailNode = self.dummy_tail["prev"]
            del self.memo[tailNode["key"]]
            self.removeSelfNode(tailNode)
            # need to add new node
        
        new_node = self.createNode(value, key)
        self.memo[key] = new_node
        self.moveNodeToHead(new_node)
        return