class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = float('inf')
        count = 0

        for num in nums:
            if ans != num:
                if count > 0:
                    count -= 1
                else:
                    ans = num
                    count = 1
            else:
                count += 1
        return ans