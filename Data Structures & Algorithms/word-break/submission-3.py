class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}

        def dfs(i):
            if i in dp:
                return dp[i]
            for w in wordDict:
                l = len(w)
                if s[i:l+i] == w and dfs(i+l):
                    dp[i] = True
            if i not in dp:
                dp[i] = False
            return dp[i]

        return dfs(0)