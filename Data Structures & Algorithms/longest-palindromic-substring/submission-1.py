class Solution:
    def checkPali(self, word, idx):
        left, right = idx, idx
        l = len(word)
        while left-1 >= 0 and word[left] == word[left-1]:
            left -= 1
        while right+1 < l and word[right] == word[right+1]:
            right += 1

        while 0 <= left and right < l and word[left] == word[right]:
            left -= 1
            right += 1
            
        return [left+1, right-1]

    def longestPalindrome(self, s: str) -> str:
        ansL, ansR = 0, 0
        
        for i in range(len(s)):
            temp = self.checkPali(s, i)

            if temp[1]-temp[0] > ansR - ansL:
                ansR = temp[1]
                ansL = temp[0]

        
        return s[ansL:ansR+1:1]

            