class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abba
        left = 0
        strDic = dict()
        maxLen = 0
        for right in range(len(s)):
            if s[right] not in strDic:
                strDic[s[right]] = right
                maxLen = max(maxLen, right - left + 1)
            else:
                newLeft = strDic[s[right]] + 1
                while left < newLeft:
                    del strDic[s[left]]
                    left += 1
                strDic[s[right]] = right
                
        return maxLen
