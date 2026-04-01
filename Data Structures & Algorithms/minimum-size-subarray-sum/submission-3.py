class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        l = 0
        total = 0
        minLen = float('inf')
        for idx, num in enumerate(nums):
            total += num
            while total >= target:
                minLen = min(minLen, idx-l+1)
                if l < len(nums):
                    total -= nums[l]
                    l += 1
                    
        return minLen if minLen < float('inf') else 0
            
                    
                
            