class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 0,1,2..., n  (首項用不到)
        m = len(edges)
        roots = [i for i in range(m+1)]
        ranks = [0] * (m+1)
        def find(n):
            while roots[n] != roots[roots[n]]:
                roots[n] = roots[roots[n]]
            return roots[n]
        ans = [None, None]
        def union(x, y):
            rootX, rootY = find(x), find(y)
            print(rootX, rootY)
            if rootX == rootY:
                ans[0], ans[1] = x, y
                return 

            if ranks[rootX] > ranks[rootY]:
                roots[rootY] = roots[rootX]
            elif ranks[rootX] < ranks[rootY]:
                roots[rootX] = roots[rootY]
            else:
                roots[rootX] = roots[rootY]
                ranks[rootX] += 1
        
        for x, y in edges:
            union(x, y)
        return ans