class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        resSet = set()
        ans = []
        n = len(nums)
        def dfs(idx, curr):
            if idx == n:
                tempSort = tuple(sorted(curr))
                if tempSort not in resSet:
                    ans.append(curr.copy())
                    resSet.add(tempSort)
                return
            curr.append(nums[idx])
            dfs(idx+1, curr)
            curr.pop()
            dfs(idx+1, curr)
            
        dfs(0, [])
        return ans