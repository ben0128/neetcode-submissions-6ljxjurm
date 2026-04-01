class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        zeroStack = []
        for idx, item in enumerate(s):
            if item == '(':
                leftStack.append(idx)
            elif item == '*':
                zeroStack.append(idx)
            else:
                if leftStack:
                    leftStack.pop()
                elif zeroStack:
                    zeroStack.pop()
                else:
                    return False
        if len(leftStack) > len(zeroStack):
            return False

        while leftStack and zeroStack:
            if leftStack[-1] < zeroStack[-1]:
                leftStack.pop()
                zeroStack.pop()
            else:
                return False
        return  len(leftStack) == 0
