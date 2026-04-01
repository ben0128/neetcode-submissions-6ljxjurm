class MinStack:

    def __init__(self):
        self.stack = []
        self.preflixMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.preflixMin:
            self.preflixMin.append(val)
        else:
            currMin = self.preflixMin[-1]
            if currMin >= val:
                self.preflixMin.append(val)
            else:
                self.preflixMin.append(currMin)

    def pop(self) -> None:
        self.stack.pop()
        self.preflixMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.preflixMin[-1]        
