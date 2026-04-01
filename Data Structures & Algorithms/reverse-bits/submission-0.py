class Solution:
    def reverseBits(self, n: int) -> int:
        ans = ''
        newNum = bin(n)[2:]
        n = len(newNum)
        for num in newNum[::-1]:
            ans += num
        for _ in range(32-n):
            ans += '0'
        return int(ans, 2)
            
