class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        disMap = defaultdict(list)
        for x,y,z in times:
            disMap[x].append((y, z))

        # 用來紀錄每個點當前最小時間
        visited = set()
        # 前面是點,後面是當前路線到這點最小時間
        min_heap = [(0, k)]
        res = 0
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            print('time', time, 'node', node, visited, res)
            if node in visited:
                continue
            res = time
            visited.add(node)

            for node2, time2 in disMap[node]:
                if node2 in visited:
                    continue
                heapq.heappush(min_heap, (time2+time, node2))
        
        print(res, visited)
        return res if len(visited) == n else -1

        



