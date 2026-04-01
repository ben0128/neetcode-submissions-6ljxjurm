class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for idx in range(n+1):
            ans[idx] = ans[idx >> 1] + (idx & 1)
        return ans
            