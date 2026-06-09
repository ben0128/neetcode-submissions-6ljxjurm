class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        ans = []
        fLen , sLen = len(firstList), len(secondList)
        # 4, 4
        if fLen == 0 or sLen == 0:
            return ans
        
        f, s = 0, 0
        # 1, 0 
        while f < fLen and s < sLen:
            fS, fE = firstList[f]
            sS, sE = secondList[s]
            tmpS, tmpE = max(fS, sS), min(fE, sE)
                
            if tmpS <= tmpE:
                ans.append([tmpS, tmpE])

            if fE > sE:
                s += 1
            else:
                f += 1
        return ans