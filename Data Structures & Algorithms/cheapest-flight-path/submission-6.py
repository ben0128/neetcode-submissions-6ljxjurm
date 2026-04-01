class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for a, b, c in flights:
            graph[a].append((b, c))
        
        min_dis = [float('inf') for _ in range(n)]

        count = 0
        temp = deque([(0, src)])
        while temp and count < k+1:
            for _ in range(len(temp)):
                currDis, node = temp.popleft()
                for nextNode, nextDis in graph[node]:
                    if min_dis[nextNode] > nextDis+currDis:
                        min_dis[nextNode] = nextDis+currDis
                        temp.append((nextDis+currDis, nextNode))
            count += 1
        return min_dis[dst] if min_dis[dst] != float('inf') else -1