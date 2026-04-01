class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if currNode.children.get(idx) == None:
                currNode.children[idx] = TrieNode()
            currNode = currNode.children[idx]
        currNode.end = True

        return


    def search(self, word: str) -> bool:
        currNode = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not currNode.children.get(idx):
                return False
            else:
                currNode = currNode.children[idx]

        return currNode.end

    def startsWith(self, prefix: str) -> bool:

        currNode = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not currNode.children.get(idx):
                return False
            else:
                currNode = currNode.children[idx]

        return True
        