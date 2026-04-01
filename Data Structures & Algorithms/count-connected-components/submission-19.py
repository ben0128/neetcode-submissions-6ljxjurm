class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # [0, 1, 2, 3, 4..., n-1]
        rootList = [root for root in range(n)]

        # [x, y] : x <= y

        def find(x):
            if x != rootList[x]:
                rootList[x] = find(rootList[x])
            return rootList[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                rootList[rootY] = rootX
        
        for a, b in edges:
            union(a, b)

        return len(set([find(node) for node in rootList]))


        