class Solution:
    

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        def calOrd(char):
            return ord('a') <= ord(char) <= ord('z') or 0 <= ord(char)-ord('0') <= 9

        filteredS = ''
        for word in s:
            if calOrd(word):
                filteredS += word
        
        return filteredS == filteredS[::-1]


