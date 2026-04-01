class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        strDic = dict()
        maxLen = 0
        for right in range(len(s)):
            if s[right] in strDic and strDic[s[right]] >= left:
                left = strDic[s[right]] + 1
            else:
                maxLen = max(maxLen, right - left + 1)
            strDic[s[right]] = right
                
        return maxLen
