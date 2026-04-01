class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        def dfs(i):
            if i == goal:
                return True
            jumpRange = range(nums[i])
            
            for step in jumpRange:
                if dfs(i+step+1):
                    return True
            return False

        return dfs(0)