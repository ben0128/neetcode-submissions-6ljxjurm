class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        needLen = len(s1)
        l = 0
        comp = defaultdict(int)
        for r, s in enumerate(s2):
            if s not in c1:
                comp = defaultdict(int)
                l = r+1
            else:
                comp[s] += 1
                
                while comp[s] > c1[s]:
                    comp[s2[l]] -= 1
                    l += 1
                print(comp, r-l+1)
                if r-l+1 == needLen:
                    return True

        return False