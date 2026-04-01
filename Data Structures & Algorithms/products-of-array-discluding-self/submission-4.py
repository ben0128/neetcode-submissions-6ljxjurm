class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resL = [1 for i in range(len(nums))]
        resR = [1 for i in range(len(nums))]
        for idx in range(len(nums)):
            if (idx == 0): 
                continue
            resL[idx] = resL[idx-1] * nums[idx-1];
            resR[len(nums)-idx-1] = resR[len(nums)-idx] * nums[len(nums)-idx]
        return [resL[i]*resR[i] for i in range(len(nums))]
