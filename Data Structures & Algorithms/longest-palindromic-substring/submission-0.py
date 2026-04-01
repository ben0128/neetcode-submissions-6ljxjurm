class Solution:
    def checkPali(self, word, idx1, idx2):
        left, right = idx1, idx2
        l = len(word)
        while 0 <= left and right < l:
            print(left, right)
            if word[left] != word[right]:
                break
            left -= 1
            right += 1
            
        return [left+1, right-1]

    def longestPalindrome(self, s: str) -> str:
        ansL, ansR = 0, 0
        
        for i in range(len(s)):
            temp = self.checkPali(s, i, i)
            temp2 = self.checkPali(s, i, i+1)

            if temp[1]-temp[0] > ansR - ansL:
                ansR = temp[1]
                ansL = temp[0]
            if temp2[1]-temp2[0] > ansR - ansL:
                ansR = temp2[1]
                ansL = temp2[0]

        
        return s[ansL:ansR+1:1]

            