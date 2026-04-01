class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
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

        ans = []
        n = len(digits)
        def backtracing(i, tmp):
            if n == i:
                ans.append(''.join(tmp))
                return
            
            for digit in hashMap[digits[i]]:
                tmp.append(digit)
                backtracing(i+1, tmp)
                tmp.pop()
            return 
        backtracing(0, [])
        return ans