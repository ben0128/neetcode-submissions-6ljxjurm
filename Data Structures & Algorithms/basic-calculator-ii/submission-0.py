class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        prev_op = '+'
        num = 0
        n = len(s)
        def applyOperators(value):
            if prev_op == '+':
                stack.append(value)
            elif prev_op == '-':
                stack.append(-value)
            elif prev_op == '*':
                stack[-1] *= value
            elif prev_op == '/':
                stack[-1] = int(stack[-1] / value)

        for i, c in enumerate(s):
            if c in '+-*/':
                applyOperators(num)
                num = 0
                prev_op = c
            elif c.isdigit():
                num = num * 10 + int(c)
        applyOperators(num)
        return sum(stack)