class PrefixTree:
    def __init__(self):
        self.trie = {}
        self.maxWordLen = 0

    def insert(self, word: str) -> None:
        head = self.trie
        self.maxWordLen = max(self.maxWordLen, len(word))
        for w in word:
            if w not in head:
                head[w] = {}
            head = head[w]
        head['isEnd'] = True
        return 

    def search(self, word: str) -> bool:
        if len(word) > self.maxWordLen:
            return False
        head = self.trie
        for w in word:
            if w not in head:
                return False
            head = head[w]
        return 'isEnd' in head


    def startsWith(self, prefix: str) -> bool:
        if len(prefix) > self.maxWordLen:
            return False
        head = self.trie
        for w in prefix:
            if w not in head:
                return False
            head = head[w]
        return True