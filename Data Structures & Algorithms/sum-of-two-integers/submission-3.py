class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        int_max = 0x7FFFFFFF
        while b != 0:
            # 加完後會是1的位置 ex: 1+0
            tmp = (a ^ b) & mask
            # 加完後進位的位置 1+1
            b = ((a & b) << 1) & mask
            a = tmp
        # int_max 是最大值, 如果a比最大值還大就代表是負數(python的特色), 所以需要額外在做一次反轉
        return a if a <= int_max else ~(a ^ mask)