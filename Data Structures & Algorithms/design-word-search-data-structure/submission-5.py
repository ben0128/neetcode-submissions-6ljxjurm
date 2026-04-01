class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        n = len(word)
        head = self.tree
        
        for i, c in enumerate(word):
            if c not in head:
                head[c] = {}
            head = head[c]
        head['end'] = True

    def search(self, word: str) -> bool:
        head = self.tree
        n = len(word)
        def dfs(node, i):
            if i == n:
                return 'end' in node
            curr = word[i]
            if curr != '.' and curr not in node:
                return False
            if curr != '.':
                node = node[curr]
                return dfs(node, i+1)
            else:
                tmp = node
                for k in node.keys():
                    if k == 'end':
                        continue
                    tmp = node[k]
                    if dfs(tmp, i+1):
                        return True
                return False
        return dfs(head, 0)