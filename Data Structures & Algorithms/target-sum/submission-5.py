class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {0: 1}
        ans = 0
        for num in nums:
            temp = defaultdict(int)
            for total, count in memo.items():
                temp[total+num] += count
                temp[total-num] += count
            memo = temp
        return memo.get(target, 0)
            
