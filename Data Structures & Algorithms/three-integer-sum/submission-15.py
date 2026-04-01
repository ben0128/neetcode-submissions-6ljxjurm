class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4, -1, -1, -1, 0, 1, 2]
        res = []
        for idx, num in enumerate(nums):
            if idx-1 >= 0 and num == nums[idx-1]:
                continue
            left, right = idx+1, len(nums)-1
            while left < right:
                tempSum = num + nums[left] + nums[right]
                if tempSum == 0:
                    res.append([nums[idx], nums[left], nums[right]])
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    while right > left and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    right -= 1
                elif tempSum > 0:
                    right -= 1
                else:
                    left += 1
        return res

            





            

        
        