class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        # same level need avoid duplicate
        # record result of every level
        def backtracing(i, tmp):
            
            ans.append(tmp.copy())
            for k, num in enumerate(nums[i:], i):
                if k > i and num == nums[k-1]:
                    continue
                tmp.append(num)
                backtracing(k+1, tmp)
                tmp.pop()
            return
        backtracing(0, [])
        return ans
            