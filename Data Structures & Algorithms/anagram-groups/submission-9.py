class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print('cba', sorted('cba'))
        # lowerCase a,b, ....z => 26 types
        # 1 < len(strs) <= 1000
        # 0 < len(str) < 100
        # focus on type and number
        ans = defaultdict(list)
        for word in strs:
            nWord = ''.join(sorted(word))
            ans[nWord].append(word)
        # in any order 
        return [ li for li in ans.values()]
        