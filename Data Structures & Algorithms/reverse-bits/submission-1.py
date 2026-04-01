class Solution:
    def reverseBits(self, n: int) -> int:
        num = str(bin(n)[2:])[::-1]
        return int(num + '0' * (32-len(num)), 2)