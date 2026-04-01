class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        # nums=[-4,-1,-1,0,1,2]
        for i in range(n-2):
            j,k = i+1, n-1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j+1 < n and nums[j] == nums[j+1]:
                        j += 1
                    while k-1 >= 0 and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                    j += 1
        return ans
