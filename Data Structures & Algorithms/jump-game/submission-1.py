class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        visited = set()
        def dfs(i):
            if i == goal:
                return True
            if i in visited:
                return False
            jumpRange = range(nums[i])
            
            for step in jumpRange:
                if dfs(i+step+1):
                    return True
            return False

        return dfs(0)