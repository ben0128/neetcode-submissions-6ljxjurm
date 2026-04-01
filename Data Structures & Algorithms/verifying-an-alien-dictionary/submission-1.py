class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {order[i]: i for i in range(len(order))}
        def cmp(s1, s2):
            for x, y in zip(s1, s2):
                if x != y:
                    return rank[x] < rank[y]
            return len(s1) <= len(s2)

        for i in range(len(words)-1):
            if not cmp(words[i], words[i+1]):
                return False
        return True
