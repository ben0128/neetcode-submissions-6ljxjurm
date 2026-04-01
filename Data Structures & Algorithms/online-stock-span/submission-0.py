class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        self.s.append(price)
        for idx in range(len(self.s)-1, -1, -1):
            if self.s[idx] > price:
                return len(self.s) - idx - 1
        return len(self.s)

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)