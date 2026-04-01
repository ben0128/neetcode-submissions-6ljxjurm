class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        ans = 0

        
        for idx, word in enumerate(s):
            r = idx+1
            while r <= l:
                if s[idx: r] == s[idx: r][::-1]:
                    ans += 1
                r += 1
        return ans


