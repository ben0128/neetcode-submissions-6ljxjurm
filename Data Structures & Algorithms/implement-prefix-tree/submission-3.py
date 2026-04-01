class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        n = len(word)
        head = self.tree
        for idx, c in enumerate(word):
            if c not in head:
                head[c] = {}
            head = head[c]
            if idx == n-1:
                head['end'] = True

    def search(self, word: str) -> bool:
        n = len(word)
        head = self.tree
        for idx, c in enumerate(word):
            if c not in head:
                return False
            head = head[c]
            if idx == n-1:
                if 'end' in head:
                    return True
                else:
                    return False

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        head = self.tree
        for idx, c in enumerate(prefix):
            if c not in head:
                return False
            if idx == n-1:
                return True
            head = head[c]
            
                


        
        