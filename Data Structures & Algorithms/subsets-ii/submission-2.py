class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        resSet = set()
        ans = []
        nums.sort()
        n = len(nums)

        def dfs(idx, curr):
            if idx == n:
                temp = tuple(curr)
                if temp not in resSet:
                    ans.append(curr.copy())
                    resSet.add(temp)
                return
            curr.append(nums[idx])
            dfs(idx+1, curr)
            curr.pop()
            dfs(idx+1, curr)
            
        dfs(0, [])
        return ans