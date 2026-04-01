class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '' or len(t) > len(s):
            return ''

        needMap = defaultdict(int)
        for wordt in t:
            needMap[wordt] += 1
        needCount = len(needMap)
        
        haveMap = defaultdict(int)
        haveCount = 0
        left, right = 0, 0
        res, resLen = [-1, -1], float('inf')
        for right in range(len(s)):
            haveMap[s[right]] += 1

            if s[right] in needMap and haveMap[s[right]] == needMap[s[right]]:
                haveCount += 1
                
                while haveCount == needCount:
                    if right+1-left < resLen:
                        res = [left, right]
                        resLen = right+1-left
                    haveMap[s[left]] -= 1

                    if s[left] in needMap and haveMap[s[left]] < needMap[s[left]]:
                        haveCount -= 1
                    left += 1
            right += 1
        print(res)
        return '' if res[0] == -1 else s[res[0]:res[1]+1]
            
