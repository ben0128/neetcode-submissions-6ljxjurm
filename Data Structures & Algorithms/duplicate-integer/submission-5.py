class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         numset = {*nums}
         return True if len(numset) != len(nums) else False