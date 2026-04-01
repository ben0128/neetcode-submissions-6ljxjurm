class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {};
        for s in strs:
            temp = ''.join(sorted(s))
            dic.setdefault(temp, []).append(s);
        return dic.values()
    
