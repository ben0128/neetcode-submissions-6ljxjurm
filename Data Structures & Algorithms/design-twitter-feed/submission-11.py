class Twitter:

    def __init__(self):
        self.time = 0
        self.userPost = defaultdict(list)
        self.follower = defaultdict(set) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPost[userId].append((-self.time, userId, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        me = self.userPost[userId]
        minH = []
        if me:
            t, u, p = me[-1]
            n = len(me)
            heapq.heappush(minH, (t, u, n-1))

        for u in self.follower[userId]:
            ps = self.userPost[u]
            if ps:
                latest = ps[-1]
                n = len(ps)
                heapq.heappush(minH, (latest[0], latest[1], n-1))
        
        ans = []
        for _ in range(10):
            if minH:
                t, u, p = heapq.heappop(minH)
                li = self.userPost[u]
                ans.append(li[p][2])
                np = p - 1
                if np >= 0:
                    nt, u, _ = self.userPost[u][np]
                    heapq.heappush(minH, (nt, u, np))
            else:
                break
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
	        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)
