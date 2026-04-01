class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        minium = float('inf')
        tempMin = float('inf')
        maxium =  -float('inf')
        tempMax = -float('inf') 
        for num in nums:
            total += num
            tempMin = min(tempMin +num, num)
            minium = min(tempMin, minium)
            tempMax = max(tempMax+num, num)
            maxium = max(tempMax, maxium)
        return max(total - minium, maxium) if total - minium > 0 else maxium
        