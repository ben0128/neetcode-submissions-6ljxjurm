class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        def backrtracing(i, tmp, total):
            # total == target:
            if total == target:
                ans.append(tmp.copy())
                return True

            for k, num in enumerate(nums[i:], i):
                newTotal = total+num
                if newTotal > target:
                    break
                tmp.append(num)
                res = backrtracing(k, tmp, newTotal)
                tmp.pop()
                if not res:
                    break
            return True
        
        backrtracing(0, [], 0)
        return ans


        # 2
        # 2
        # 2
        # 2
        # 2
