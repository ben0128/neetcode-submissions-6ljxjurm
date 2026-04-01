class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        ans = 0
        numDict = defaultdict(list)
        for idx, word in enumerate(s):
            numDict[word].append(idx)
        print(numDict)
        for idx, word in enumerate(s):
            for i in numDict[word][::-1]:
                print(s[idx:i+1], s[idx:i+1][::-1])
                if i < idx:
                    break
                
                if word == s[i] and s[idx:i+1] == s[idx:i+1][::-1]:
                    ans += 1
        return ans


