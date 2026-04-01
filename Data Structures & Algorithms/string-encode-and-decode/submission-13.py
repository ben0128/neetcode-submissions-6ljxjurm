class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        for idx, char in enumerate(s):
            if char == '#' and i <= idx:
                tempLen = int(s[i:idx])
                res.append(s[idx+1:tempLen+idx+1])
                i = idx+tempLen+1
        return res

