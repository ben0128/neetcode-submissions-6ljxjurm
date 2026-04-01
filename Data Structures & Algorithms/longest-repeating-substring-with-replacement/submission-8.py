class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n-1:
            return n

        l, maxL = 0, 0
        freq = [0] * 26
        baseA = ord('A')
        for r in range(n):
            idx = ord(s[r]) - baseA
            freq[idx] += 1
            tmpL, total = max(freq), sum(freq)
            if total - tmpL <= k:
                maxL = max(maxL, total)
            else:
                j = ord(s[l]) - baseA
                freq[j] -= 1
                l += 1

        return maxL