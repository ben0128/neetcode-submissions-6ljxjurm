class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []

        def isPalindrome(word):
            return word == word[::-1]

        def dfs(idx):
            if idx == len(s):
                ans.append(part.copy())
                return 
            for j in range(idx, len(s)):
                temp = s[idx:j+1]
                if isPalindrome(temp):
                    part.append(temp)
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return ans