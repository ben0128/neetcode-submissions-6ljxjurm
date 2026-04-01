class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxF = 0
        for idx in range(len(s)):
            count[s[idx]] = 1 + count.get(s[idx], 0)
            maxF = max(maxF, count[s[idx]])
            while idx - l - maxF + 1 > k:
                count[s[l]] -= 1
                l += 1
            res = max(maxF, idx - l + 1)
        return res

