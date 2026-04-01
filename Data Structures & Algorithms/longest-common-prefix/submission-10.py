class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        preflix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(preflix):
                preflix = preflix[:len(preflix)-1]
        return preflix