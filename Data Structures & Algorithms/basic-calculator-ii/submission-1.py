class Solution:
    def calculate(self, s: str) -> int:
        lastNum = 0
        res = 0
        prev_op = '+'
        num = 0
        def applyOperators(value):
            nonlocal lastNum, res
            if prev_op == '+':
                res += lastNum
                lastNum = value
            elif prev_op == '-':
                res += lastNum
                lastNum = -value
            elif prev_op == '*':
                lastNum *= num
            elif prev_op == '/':
                lastNum = int(lastNum / num)

        for c in s:
            if c in '+-*/':
                applyOperators(num)
                num = 0
                prev_op = c
            elif c.isdigit():
                num = num * 10 + int(c)
        applyOperators(num)
        return res+lastNum
