class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = [''] * len(strs[0])

        for idx, char in enumerate(strs[0]):
            isAdd = True
            for j in range(1, len(strs)):
                if len(strs[j]) <= idx or strs[j][idx] != char:
                    isAdd = False
                    break
            if isAdd:
                res[idx] = char
            else:
                break
        return ''.join(res)