class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        record = [False] * n
        def dfs(path, visited):
            if len(path) == n:
                ans.append(path[:])
                return
            
            
            for i in range(n):
                if visited[i]:
                    continue
                if i-1 >= 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                path.append(nums[i])
                dfs(path, visited)
                path.pop()
                visited[i] = False
            return

        dfs([], record)
        return ans
