class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = 0
        for char in str(format(n, '032b')):
            if char == '1':
                temp += 1
        return temp