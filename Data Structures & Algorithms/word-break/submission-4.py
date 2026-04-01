class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}
        wordSet = set(wordDict)

        def dfs(i):
            if i in dp:
                return dp[i]

            for j in range(i, len(s)):
                if s[i:j+1] in wordSet and dfs(j+1):
                    dp[i] = True
            if i not in dp:
                dp[i] = False
            return dp[i]
        return dfs(0)