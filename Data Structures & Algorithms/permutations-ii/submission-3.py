class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        record = [False] * n
        def dfs(path):
            if len(path) == n:
                ans.append(path[:])
                return

            for i in range(n):
                if record[i]:
                    continue
                if i-1 >= 0 and nums[i] == nums[i-1] and not record[i-1]:
                    continue
                record[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                record[i] = False
            return

        dfs([])
        return ans
