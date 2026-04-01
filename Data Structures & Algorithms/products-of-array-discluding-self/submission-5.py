class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, a, ab, abc
        # bcd, cd , d
        n = len(nums)
        res = [1] * n
        s = 1
        
        for i in range(n-1):
            res[i+1] = res[i]*nums[i]
        
        for i in range(n-1, 0, -1):
            s *= nums[i]
            res[i-1] *= s
        return res