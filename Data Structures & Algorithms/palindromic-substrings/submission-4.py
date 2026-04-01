class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        ans = 0

        def calPali(word, i, j):
            l, r = i, j
            tempAns = 0
            while l >= 0 and r < len(word):
                if word[l] != word[r]:
                    break
                tempAns += 1
                l -= 1
                r += 1
            return tempAns

        for i in range(l):
            ans += calPali(s, i, i)
            ans += calPali(s, i, i+1)
        return ans


