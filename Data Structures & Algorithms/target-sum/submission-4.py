class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {0: 1}
        ans = 0
        for num in nums:
            temp = defaultdict(int)
            print(memo)
            for total in memo:
                temp[total+num] += memo.get(total, 0)
                temp[total-num] += memo.get(total, 0)
            print(temp)
            memo = temp
        print(memo)
        return memo.get(target, 0)
            
