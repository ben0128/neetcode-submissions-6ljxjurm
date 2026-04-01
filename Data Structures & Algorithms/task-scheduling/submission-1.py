class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countList = [[-count, cat] for cat, count in Counter(tasks).items()]
        time = 0
        heapq.heapify(countList)
        queue = deque()
        
        while countList or queue:
            if queue and queue[0][1] == time:
                popedQueue = queue.popleft()
                heapq.heappush(countList, popedQueue[0])
            
            if countList:  
                popEl = heapq.heappop(countList)
                popEl[0] += 1
                if popEl[0] != 0:
                    queue.append((popEl, time+n+1))
            time += 1
        return time