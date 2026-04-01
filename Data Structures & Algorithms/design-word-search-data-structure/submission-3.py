class WordDictionary:

    def __init__(self):
        self.trie = defaultdict(dict)

    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if not curr[char]:
                curr[char] = defaultdict(dict)
            
        
            curr = curr[char]
        curr['End'] = {}


    def search(self, word: str) -> bool:
        def recursive(idx, currTrie):
            if idx == len(word):
                return 'End' in currTrie

            temp = word[idx] 
            
            if temp != '.' and temp not in currTrie:
                return False
            elif temp != '.':
                return recursive(idx+1, currTrie[temp])

            for key in currTrie.keys():
                if recursive(idx+1, currTrie[key]):
                    return True
            return False

        return recursive(0, self.trie)
