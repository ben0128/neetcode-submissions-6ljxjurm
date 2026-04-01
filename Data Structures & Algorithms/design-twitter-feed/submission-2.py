class Twitter:
    def __init__(self):
        self.time = 0
        self.feed = defaultdict(list)
        self.follower = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.feed[userId], (self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feedList = self.feed[userId].copy()
        for user in self.follower[userId]:
            feedList.extend(self.feed[user])
        res = heapq.nlargest(10, feedList)

        return [item[1] for item in res]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        # followerId 追隨=> followeeId
        if followerId != followeeId:
            self.follower[followerId].add(followeeId) 


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)
