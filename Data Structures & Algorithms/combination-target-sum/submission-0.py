class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, currArr, total):
            if total == target:
                ans.append(currArr.copy())
                return
            if i > len(nums)-1 or total > target:
                return
            
            currArr.append(nums[i])
            dfs(i, currArr, total+nums[i])
            currArr.pop()
            dfs(i+1, currArr, total)

        dfs(0, [], 0)
        return ans

            

# ans = [[9], [2, 2, 5]]
        # [2, 5, 6, 9]
        # [[2], [5], [6]]
        # [[2, 2], [2, 5], [2, 6]]
        # [[2, 2, 2]]
        # [[2, 2, 2, 2]]
        # 