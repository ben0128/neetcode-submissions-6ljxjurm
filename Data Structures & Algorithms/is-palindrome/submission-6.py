class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        right = len(s)-1
        alphStart = ord('a')
        alphEnd = ord('z')
        numStart = ord('0')
        numEnd = ord('9')
        idx = 0
        while idx < right:
            if (alphEnd >= ord(s[idx]) >= alphStart) or (numEnd >= ord(s[idx]) >= numStart):
                while not ((alphEnd >= ord(s[right]) >= alphStart) or (numEnd >= ord(s[right]) >= numStart)):
                    right -= 1
                if s[right] != s[idx]:
                    print(s[right], s[idx])
                    return False
                else:
                    right -= 1
            idx += 1
        return True


                