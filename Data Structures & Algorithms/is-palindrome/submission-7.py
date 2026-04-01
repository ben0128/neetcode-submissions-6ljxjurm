class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        right = len(s)-1
        idx = 0
        while idx < right:
            if s[idx].isalnum():
                while not s[right].isalnum():
                    right -= 1
                if s[right] != s[idx]:
                    return False
                else:
                    right -= 1
            idx += 1
        return True


                