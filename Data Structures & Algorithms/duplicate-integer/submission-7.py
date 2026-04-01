class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # step1: init set
        numSet = set()

        # step2: foreach nums
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)
        return False