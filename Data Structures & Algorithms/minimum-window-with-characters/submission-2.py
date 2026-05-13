class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if n < len(t):
            return ''
        curr = defaultdict(int)
        need = defaultdict(int)
        valid = 0

        for c in t:
            need[c] += 1
        
        needLen = len(need)
        l = 0
        ans = [0, n]
        for r, c in enumerate(s):
            curr[c] += 1
            if curr[c] == need[c]:
                valid += 1
            
            while valid == needLen:
                if ans[1]-ans[0] > r-l:
                    ans = [l, r]
                waitRemove = s[l]
                curr[waitRemove] -= 1
                if curr[waitRemove] < need[waitRemove]:
                    valid -= 1
                l += 1

        return s[ans[0]:ans[1]+1] if ans[1] != n else ''