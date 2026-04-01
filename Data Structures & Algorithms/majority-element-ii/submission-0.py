class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3
        ans = []
        record = defaultdict(int)
        for num in nums:
            record[num] += 1
            if num not in ans and record[num] > limit:
                ans.append(num)
                if len(ans) == 2:
                    return ans
        return ans