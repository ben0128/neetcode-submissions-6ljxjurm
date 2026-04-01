class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countList = [[-count, cat] for cat, count in Counter(tasks).items()]
        time = 0
        heapq.heapify(countList)
        queue = deque()
        print(countList, queue)
        
        while countList:
            popEl = heapq.heappop(countList)
            popEl[0] += 1
            if popEl[0] != 0:
                queue.append((popEl, time+n+1))
            time += 1
            while not countList and queue and queue[0][1] != time:
                time += 1
            if queue and queue[0][1] == time:
                popedQueue = queue.popleft()
                heapq.heappush(countList, popedQueue[0])
            
        return time
        
# [(-2, 'X'), (-2, 'Y')]
# 