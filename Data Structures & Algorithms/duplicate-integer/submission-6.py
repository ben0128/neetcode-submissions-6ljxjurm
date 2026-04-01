class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         return True if len({*nums}) != len(nums) else False