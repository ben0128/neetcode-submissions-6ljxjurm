class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # cat => sorted(cat) => act

        # step1 : strMap = {[sorted(string)]: [] }
        strMap = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(list(word)))
            strMap[key].append(word)
        return list(strMap.values())