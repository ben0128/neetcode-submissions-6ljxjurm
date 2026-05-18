class Solution:
    def climbStairs(self, n: int) -> int:
        # steps = [0] * (n+1)
        if n <= 2:
            return n
        
        fir, sec = 1, 2
        # n >= 3
        # fir = 2, sec = 3
        for _ in range(3, n+1):
            curr = fir + sec
            fir = sec
            sec = curr
        return sec
    # TC = O(n) , SC = O(n) => O(1)
    # n = 1,  1 => 1
    # n = 2,  1+1, 2 => 2
    # n = 3,  1+2, 2+1, 1+1+1 => 3
    # n = 4   1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 => 5
    # print('1', climbStairs(1) == 1)
    # print('2', climbStairs(2) == 2)
    # print('3', climbStairs(3) == 3)
    # print('4', climbStairs(4) == 5)