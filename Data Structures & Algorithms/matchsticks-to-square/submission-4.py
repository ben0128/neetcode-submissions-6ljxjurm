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
                return True

            seen = set()
            for j in range(4):
                if buckets[j] >= matchsticks[i] and buckets[j] not in seen:
                    
                    buckets[j] -= matchsticks[i]
                    if dfs(i+1, buckets):
                        return True
                    buckets[j] += matchsticks[i]
                    seen.add(buckets[j])
                if buckets[j] == need:
                    break
            return False
            
        return dfs(0, [need] * 4)