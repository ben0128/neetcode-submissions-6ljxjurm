class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        memo = 0

        for num in nums:
            if memo >> num & 1 == 1:
                return num
            memo |= 1 << num
        