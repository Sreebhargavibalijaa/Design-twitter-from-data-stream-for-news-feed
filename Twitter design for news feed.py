#Designing the twitter news feed from data stream
class Twitter:
    import heapq
    def __init__(self):
        self.tweet_id_user_id = collections.defaultdict(collections.deque) #tweet ids
        self.followee_followers = collections.defaultdict(set) #tweet ids
    def postTweet(self, userId: int, tweetId: int) -> None:       
        if(len(self.tweet_id_user_id[userId])<10):#each time we just need 10 recent tweets for specific user

            self.tweet_id_user_id[userId].append(tweetId)
        else:
            # q= deque(self.tweet_id[userId])
            self.tweet_id_user_id[userId].popleft()
            self.tweet_id_user_id[userId].append(tweetId)
            

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        u = self.tweet_id_user_id[userId]
		h.extend(u)
        heapify(h)
        for user in self.followee_followers[userId]:
            tweets = self.tweet_id_user_id[user]
            for x in range(len(tweets) - 1, -1, -1):
                if len(h) < 10:
                    heappush(h, tweets[x])
                else:
                    if h[0][0] < tweets[x][0]:
                        heappushpop(h, tweets[x])
                    else:
                        break
        return [heappop(h)[1] for x in range(len(h))][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followee_followers[followerId].discard(followeeId)