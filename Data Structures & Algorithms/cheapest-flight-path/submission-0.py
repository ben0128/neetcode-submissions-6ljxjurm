class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        print('src', src)
        graph = defaultdict(list)

        for a, b, c in flights:
            graph[a].append((b, c))
        
        min_dis = [float('inf') for _ in range(n)]

        count = 0
        print('src', src)
        temp = deque([(0, src)])
        print('temp',temp)
        while temp and count < k+1:
            for _ in range(len(temp)):
                currDis, node = temp.popleft()
                print(currDis, node)
                for nextNode, nextDis in graph[node]:
                    print(node, nextNode, nextDis)
                    if min_dis[nextNode] > nextDis+currDis:
                        min_dis[nextNode] = nextDis+currDis
                        temp.append((nextDis+currDis, nextNode))
            count += 1
        print(min_dis)
        return min_dis[dst] if min_dis[dst] != float('inf') else -1



        
