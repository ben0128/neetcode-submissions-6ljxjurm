class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            for j in range(i+1, n+1):
                if s[i:j] in wordSet:
                    dp[j] = True
        return dp[-1]