class Solution:
    def dp(self, left, right, li):
        rob1, rob2 = 0, 0
        for i in range(left, right):
            temp = max(li[i]+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = len(nums)
        tempAns1 = self.dp(0, l-1, nums)

        tempAns2 = self.dp(1, l, nums)

        return max(tempAns1, tempAns2)