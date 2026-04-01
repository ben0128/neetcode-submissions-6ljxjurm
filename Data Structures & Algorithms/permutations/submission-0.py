class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        def dfs(curr):
            if len(curr) == length:
                ans.append(list(curr.keys()))
                return

            for num in nums:
                if num not in curr:
                    curr[num] = True
                    dfs(curr)
                    del curr[num]

        dfs(dict())
        return ans

