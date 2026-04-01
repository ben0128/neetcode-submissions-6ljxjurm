
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a,b):
            return a+b
        def sub(a,b):
            return a-b
        def mul(a,b):
            return a*b
        def div(a,b):
            return int(a/b)
        op = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
        }
        s = []
        for c in tokens:
            if c not in op:
                s.append(int(c))
            else:
                b, a = s.pop(), s.pop()
                s.append(op[c](a,b))
            
        return s[-1]