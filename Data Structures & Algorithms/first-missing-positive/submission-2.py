class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(n):
            temp = abs(nums[i])
            if 1 <= temp <= n:
                if nums[temp-1] > 0:
                    nums[temp-1] *= -1
                elif nums[temp-1] == 0:
                    nums[temp-1] = -1
        for i in range(n):
            if nums[i] >= 0:
                return i+1
        return n+1

