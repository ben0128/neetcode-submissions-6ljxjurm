class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            tmp = [1]
            for j in range(i+1, len(nums)):
                if i == 0:
                    print(nums[j])
                if nums[j] > nums[i]:
                    tmp.append(dp[j]+1)
            print(i, tmp)
            dp[i] = max(tmp)
        return max(dp)