class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        def backtracing(i, tmp, total):
            if target == total:
                ans.append(tmp.copy())
                return

            for k, num in enumerate(candidates[i:], i):
                newTotal = num+total
                if newTotal > target:
                    break
                if k > i and num == candidates[k-1]:
                    continue
                tmp.append(num)
                backtracing(k+1, tmp, newTotal)
                tmp.pop()
            return 

        backtracing(0, [], 0)
        return ans