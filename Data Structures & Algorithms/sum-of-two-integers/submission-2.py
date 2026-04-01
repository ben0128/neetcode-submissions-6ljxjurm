class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        int_max = 0x7FFFFFFF
        while b != 0:
            tmp = (a ^ b) & mask
            b = ((a & b) << 1) & mask
            a = tmp
        return a if a <= int_max else ~(a ^ mask)