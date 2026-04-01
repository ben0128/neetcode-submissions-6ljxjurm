class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, res = [], 0

        for item in operations:
            if item not in ["+", "D", "C"]:
                stack.append(int(item))
                res += int(item)
            elif item == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif item == "D":
                res += stack[-1]*2
                stack.append(stack[-1]*2)
            elif item == "C":
                res -= stack.pop()
                
        return res
