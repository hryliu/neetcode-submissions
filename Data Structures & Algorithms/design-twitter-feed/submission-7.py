class Twitter:

    def __init__(self):
        self.tweet_count = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list[tuple])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.tweet_count, tweetId))
        self.tweet_count += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = list(self.tweets[userId][-10:])
        recent_tweets = []
        for u in self.following[userId]:
            all_tweets.extend(self.tweets[u][-10:])

        heapq.heapify(all_tweets)

        for i in range(10):
            if all_tweets:
                popped = heapq.heappop(all_tweets)
                recent_tweets.append(popped[1])

        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
        
