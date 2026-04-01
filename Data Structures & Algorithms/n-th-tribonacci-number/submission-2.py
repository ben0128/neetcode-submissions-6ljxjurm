class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        if n == 2:
            return 1
        fir, sec, thr = 0, 1, 1
        temp = 0
        for num in range(3, n+1):
            temp = fir + sec + thr
            fir = sec
            sec = thr
            thr = temp
        return temp

        
