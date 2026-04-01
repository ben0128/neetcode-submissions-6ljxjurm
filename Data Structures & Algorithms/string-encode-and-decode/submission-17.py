class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for char in strs:
            res.append(f"{len(char)}%{char}")
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        num = 0
        idx = 0
        l = len(s)
        res = []
        while idx < l:
            char = s[idx]
            if char == '%':
                res.append(s[idx+1: idx+1+num])
                idx += num
                num = 0
            else:
                num = num*10 + int(char)
            idx += 1
        return res