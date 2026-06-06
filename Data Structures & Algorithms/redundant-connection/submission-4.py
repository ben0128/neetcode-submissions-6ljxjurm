class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 0,1,2..., n  (首項用不到)
        m = len(edges)
        roots = [i for i in range(m+1)]
        ranks = [0] * (m+1)
        def find(n):
            curr = n
            while curr != roots[curr]:
                roots[curr] = roots[roots[curr]]
                curr = roots[curr]
            return curr
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return [x, y]

            if ranks[rootX] > ranks[rootY]:
                roots[rootY] = roots[rootX]
            elif ranks[rootX] < ranks[rootY]:
                roots[rootX] = roots[rootY]
            else:
                roots[rootX] = roots[rootY]
                ranks[rootY] += 1
            return None
        
        for x, y in edges:
            if union(x, y) is not None:
                return [x, y]