class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        disMap = defaultdict(list)
        for x,y,z in times:
            disMap[x].append((y, z))
        print(disMap)

        dist = { node: float("inf") for node in range(1, n+1)}
        temp = deque([(k, 0)])
        dist[k] = 0
        while temp:
            print(temp)
            el, currTime = temp.popleft()
            if dist[el] < currTime:
                continue
            for nextEl, nextTime in disMap[el]:
                newTime = currTime + nextTime
                if newTime < dist[nextEl]:
                    dist[nextEl] = newTime
                    temp.append([nextEl, newTime])
        
        res = max(dist.values())
        return res if res < float('inf') else -1



