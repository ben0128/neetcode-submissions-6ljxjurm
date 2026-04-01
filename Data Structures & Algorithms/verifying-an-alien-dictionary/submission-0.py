class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charMap = {order[i]: i for i in range(len(order))}
        def cmp(word):
            return [ charMap[char] for char in word]
        newWords = sorted(words, key=cmp)
        return words == newWords