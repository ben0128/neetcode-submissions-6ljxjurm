class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        stack = []
        sMap = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        for i, char in enumerate(s):
            if char not in sMap:
                stack.append(char)
            else:
                if not stack or stack.pop() != sMap[char]:
                    return False
        return len(stack) == 0