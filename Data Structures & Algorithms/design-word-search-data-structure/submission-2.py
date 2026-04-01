class WordDictionary:

    def __init__(self):
        self.trie = defaultdict(dict)

    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if not curr[char]:
                curr[char] = defaultdict(list)
            
            
            curr = curr[char]
        curr['End'] = {}


    def search(self, word: str) -> bool:
        def recursive(idx, currTrie):
            if idx == len(word) and 'End' in currTrie:
                return True
            elif idx == len(word):
                return False
            temp = word[idx] 
            
            if temp != '.' and temp not in currTrie:
                return False
            elif temp != '.':
                nextTrie = currTrie[temp]
                return recursive(idx+1, nextTrie)

            for key in currTrie.keys():
                if recursive(idx+1, currTrie[key]):
                    return True
            return False

        return recursive(0, self.trie)
