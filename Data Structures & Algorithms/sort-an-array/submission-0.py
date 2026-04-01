class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # { num: count}
        countMap = defaultdict(int)

        # for loop { 5: 1, 10: 1, 2: 1, 1: 1, 3: 1}
        max_num, min_num = -50001, 50001
        for num in nums:
            countMap[num] += 1
            max_num = max(max_num, num)
            min_num = min(min_num, num)
            
        ans = [None] * len(nums)
        # for loop 
        idx = 0
        for curr in range(min_num, max_num+1):
            while countMap[curr] != 0:
                countMap[curr] -= 1
                ans[idx] = curr
                idx += 1
        return ans