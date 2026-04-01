class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # [0, 1, 2, 3, 4..., n-1]
        rootList = [root for root in range(n)]

        # [x, y] : x <= y

        def find(x):
            tmp = x
            while rootList[tmp] != tmp:
                tmp = rootList[tmp]
            return tmp

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                rootList[rootY] = rootX
        
        for a, b in edges:
            union(a, b)
        
        rootList = [find(num) for num in rootList]

        return len(set(rootList))
        