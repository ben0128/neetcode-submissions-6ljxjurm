class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        ans = []
        path = ''
        hashMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(idx):
            nonlocal path
            if len(digits) == idx:
                ans.append(path)
                return
            for char in hashMap[digits[idx]]:
                path += char
                dfs(idx+1)
                path = path[:-1]
        dfs(0)
        return ans
