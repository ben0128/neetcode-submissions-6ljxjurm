class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        ans = []
        def dfs(i, curr, total):
            if total == target:
                ans.append(curr.copy())
                return
            if total > target or i > len(nums) -1:
                return

            curr.append(nums[i])
            dfs(i+1, curr, total+nums[i])
            curr.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return ans