class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) > 0 else None

    def getMin(self) -> int:
        tempMin = self.stack[0]
        for num in self.stack:
            tempMin = min(tempMin, num)
        return tempMin
