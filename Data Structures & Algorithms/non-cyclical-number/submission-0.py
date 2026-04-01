class Solution:
    def isHappy(self, n: int) -> bool:
        hist = set()
        temp = n
        while temp != 1:
            tempStr = str(temp)
            temp = 0
            for char in tempStr:
                temp += int(char) ** 2
            if temp in hist:
                return False
            else:
                hist.add(temp)
        return True