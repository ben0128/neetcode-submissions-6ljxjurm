class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numDict = {}
        starter = 0
        tmpMax = 0
        for idx, char in enumerate(s):
            if char not in numDict or numDict[char] < starter:
                numDict[char] = idx
                tmpMax = max(tmpMax, idx-starter+1)
            else:
                starter = numDict[char]+1
                numDict[char] = idx
        return tmpMax