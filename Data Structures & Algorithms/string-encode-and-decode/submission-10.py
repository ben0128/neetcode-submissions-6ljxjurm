class Solution:

    def encode(self, strs: List[str]) -> str:
        res = '';
        for s in strs:
            res += str(len(s))+ '#' + s;
        return res;
    def decode(self, s: str) -> List[str]:
        res = [];
        i = 0;
        print(s);
        for idx, char in enumerate(s):
            if char == '#' and i <= idx:
                print(i,s[i],idx, s[idx]);
                tempLen = int(s[i:idx]);
                res.append(s[idx+1:tempLen+idx+1]);
                i = idx+tempLen+1;
            if (i == len(s)): return res
        return res

