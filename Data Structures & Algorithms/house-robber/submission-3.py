class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # rob1 前前間的最大值
        # rob2 前間的最大值

        for num in nums:
            temp = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
