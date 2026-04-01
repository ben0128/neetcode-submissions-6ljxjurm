class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        d = {}
        for char in s:
            d[char] = d.setdefault(char, 0) + 1;
        for char in t:
            d[char] = d.setdefault(char, 0) - 1;
            if d[char] < 0:
                return False;
        return True