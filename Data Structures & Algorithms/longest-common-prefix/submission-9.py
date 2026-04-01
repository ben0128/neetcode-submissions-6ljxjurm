class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = {}
        head = res
        n = len(strs[0])
        for j in range(n):
            res[strs[0][j]] = {}
            res = res[strs[0][j]]
        res = head

        end = float('inf')
        for i in range(1, len(strs)):
            tempEnd = float('inf')
            for j in range(len(strs[i])):
                if n < j+1:
                    break
                if strs[i][j] not in res:
                    break
                tempEnd = j
                res = res[strs[i][j]]
            if tempEnd == float('inf'):
                return ''
            end = min(tempEnd+1, end)
            res = head
        print(end)
        return strs[0][:end] if end < float('inf') else ''
