class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L = 'abcdefghijklmnopqrstuvwxyz'
        N = '0123456789'
        def checkstr(char):
            return char in L or char in N

        n = len(s)
        i, j = 0, len(s)-1
        while i < j:
            while i < n and not checkstr(s[i]):
                i += 1

            while j > 0 and not checkstr(s[j]):
                j -= 1
            
            if i < n and j > 0 and s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True