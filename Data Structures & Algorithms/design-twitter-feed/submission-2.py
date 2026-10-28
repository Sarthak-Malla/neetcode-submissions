class Twitter:

    def __init__(self):
        self.followRecord = {}
        self.tweets = [] # list of time, userId, tweetId
        self.time = 0
        heapq.heapify(self.tweets)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.tweets, [-self.time, userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        temp = []
        res = []

        while self.tweets and len(res) < 10:
            temp.append(heapq.heappop(self.tweets))
            if userId == temp[-1][1] or (self.followRecord.get(userId) and temp[-1][1] in self.followRecord[userId]):
                res.append(temp[-1][2])
        
        for item in temp:
            heapq.heappush(self.tweets, item)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.followRecord.get(followerId):
            self.followRecord[followerId] = set([followeeId])
            return
        self.followRecord[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followRecord[followerId].discard(followeeId)
