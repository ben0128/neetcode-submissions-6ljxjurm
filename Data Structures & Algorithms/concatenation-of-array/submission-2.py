class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in range(n):
            nums.append(nums[num])
        return nums