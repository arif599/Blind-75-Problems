from heapq import heapify, heappush, heappop

class Twitter:

    def __init__(self):
        self.followers = {} # key: userID, value: set(userId)
        self.tweets = {} # key: userID, value: [(time, tweetID)]
        self.time = 1
        
        """
        time = 2
        
        followers = {
            1: set(1, 2)
        }
        
        tweets = {
            1: [(-1, 5)]
            2: [(-2, 6)]
        }
        """
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        # add time and tweet to tweets
        if userId not in self.tweets:
            self.tweets[userId] = [(-self.time, tweetId)]
        else:
            self.tweets[userId].append((-self.time, tweetId))
        
        # add user to followers
        if userId not in self.followers:
            self.followers[userId] = {userId}
            
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # join all user's followers tweets and get the most recent = higest time
        feed = [] # [(-2, 6), (-1, 5)]
        for follower in self.followers[userId]:
            for tweet in self.tweets[follower]:
                feed.append(tweet)
        heapify(feed)
        
        top = [] # 6, 5
        k = 1
        while feed and k <= 10:
            top.append(heappop(feed)[1])
            k += 1
        
        return top
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # add followee to set
        if followerId not in self.followers:
            self.followers[followerId] = {followeeId}
        else:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followee from set
        self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)