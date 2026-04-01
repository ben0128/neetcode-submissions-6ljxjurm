class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        numMap = defaultdict(int)
        ans = 0
        for num in nums:
            if num == k:
                ans += 1
            if num-k in numMap:
                ans += numMap[num-k]
            numMap[num] += 1
        return ans
