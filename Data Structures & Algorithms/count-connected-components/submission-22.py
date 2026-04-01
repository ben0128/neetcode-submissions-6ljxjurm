class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rootList = [root for root in range(n)]

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

        return len(set([find(node) for node in range(n)]))




        