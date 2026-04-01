class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        strMap = { c: set() for word in words for c in word}
        indegree = { c: 0 for c in strMap}
        n = len(words)
        for i in range(n-1):
            j = 0
            w1, w2 = words[i], words[i+1]
            l = min(len(w1), len(w2))
            if w1[:l] == w2[:l] and len(w1) > l:
                return ''
            while j < l and w1[j] == w2[j]:
                j += 1
            if j != l and w2[j] not in strMap[w1[j]]:
                indegree[w2[j]] += 1
                strMap[w1[j]].add(w2[j])

        res = []
        tmp = deque([ k for k in indegree if indegree[k] == 0])

        while tmp:
            el = tmp.popleft()
            res.append(el)
            
            for word in strMap[el]:
                indegree[word] -= 1
                print('word', word,indegree[word])
                if indegree[word] == 0:
                    tmp.append(word)
        if len(indegree) > len(res):
            return ''
        return ''.join(res)