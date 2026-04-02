class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = {}
        ans = []

        for word in words:
            head = self.trie
            for c in word:
                if c not in head:
                    head[c] = {}
                head = head[c]
            head['end'] = word

        m, n = len(board), len(board[0])
        ways = [1, 0, -1, 0, 1]

        def dfs(row, col, currTrie):
            cell = board[row][col]
            currTrie = currTrie[cell]

            if currTrie.get('end'):
                ans.append(currTrie['end'])
                currTrie['end'] = None

            board[row][col] = '.'
            for k in range(4):
                nxtR, nxtC = ways[k]+row, ways[k+1]+col
                if 0 <= nxtR < m and 0 <= nxtC < n and board[nxtR][nxtC] != '.' and board[nxtR][nxtC] in currTrie:
                    if dfs(nxtR, nxtC, currTrie):
                        return True

            board[row][col] = cell
            return False

        for i in range(m):
            row = board[i]
            for j in range(n):
                cell = row[j]
                if cell not in self.trie:
                    continue
                dfs(i, j, self.trie)
        return ans