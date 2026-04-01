class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        ans = []
        path = ''
        hashMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def dfs(idx):
            nonlocal path
            if len(digits) == idx:
                ans.append(path)
                return
            print(hashMap[digits[idx]])
            for char in hashMap[digits[idx]]:
                print(char)
                path += char
                dfs(idx+1)
                path = path[:-1]
        dfs(0)
        return ans

