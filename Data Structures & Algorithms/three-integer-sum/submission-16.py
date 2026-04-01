class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        # nums=[-4,-1,-1,0,1,2]
        i = 0
        while i < n-2:
            j,k = i+1, n-1
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                while j+1 < n and nums[j] == nums[j+1]:
                    j += 1
                while k-1 >= 0 and nums[k] == nums[k-1]:
                    k -= 1
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
                    j += 1
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ans
