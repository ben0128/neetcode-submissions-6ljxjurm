class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rootList = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            while rootList[x] != x:
                rootList[x] = rootList[rootList[x]]
                x = rootList[x]
            return rootList[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return
            if rank[rootX] > rank[rootY]:
                rootList[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                rootList[rootX] = rootY
            else:
                rootList[rootX] = rootY
                rank[rootY] += 1


        for a, b in edges:
            union(a, b)

        for idx, num in enumerate(rootList):
            rootList[idx] = find(idx)
        print(rootList)
        return len(set(rootList))


        