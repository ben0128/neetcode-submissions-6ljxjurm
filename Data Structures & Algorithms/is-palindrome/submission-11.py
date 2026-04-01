class Solution:
    

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        def calOrd(char):
            return ord('a') <= ord(char) <= ord('z') or 0 <= ord(char)-ord('0') <= 9

        filteredS = ''
        for word in s:
            if calOrd(word):
                filteredS += word
        
        left, right = 0, len(filteredS)-1
        print(filteredS)
        while left < right:
            if filteredS[left] != filteredS[right]:
                return False
            left += 1
            right -= 1
        return True


