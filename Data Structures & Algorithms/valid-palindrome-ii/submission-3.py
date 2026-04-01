class Solution:
    def validPalindrome(self, s: str) -> bool:
        isUseJump = False

        l, r = 0, len(s)-1

        def checkLoop(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    continue
                return False
            return True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue

            return checkLoop(l+1, r) or checkLoop(l, r-1)
        return True