class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = True
        n = len(digits)
        for idx in range(n):
            numStr = digits[n-idx-1]
            newNum = int(numStr) + 1 if plus else int(numStr)
            print(newNum)
            if newNum >= 10:
                newNum -= 10
                plus = True
            else:
                plus = False
            digits[n-idx-1] = str(newNum)
        if plus:
            digits.insert(0, '1')
        return digits
            


