class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for idx, num in enumerate(nums):
            total ^= (idx + 1)
            total ^= num
        return total