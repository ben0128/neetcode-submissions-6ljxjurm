class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}  
        l = 0
        maxLen = 0
        for r in range(len(s)):
            c = s[r]
            # 重複的字串在窗內 且 
            if c in charDict and charDict[c] >= l:
                l = charDict[c] + 1
            else:
                maxLen = max(maxLen, r-l+1)
            charDict[c] = r
        return maxLen