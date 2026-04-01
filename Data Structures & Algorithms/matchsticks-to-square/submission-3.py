class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        need = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > need:
            return False
        
        n = len(matchsticks)
        def dfs(i, buckets):
            if i == n:
                for bucket in buckets:
                    if bucket != 0:
                        return False
                return True

            for j in range(4):
                if buckets[j] >= matchsticks[i]:
                    buckets[j] -= matchsticks[i]
                    if not dfs(i+1, buckets):
                        buckets[j] += matchsticks[i]
                    else:
                        return True
            return False
            
        return dfs(0, [need] * 4)
