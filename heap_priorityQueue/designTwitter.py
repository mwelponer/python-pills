from typing import Optional
from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    # get last 10 tweets from the list of users userId follows, userId included
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # get the list of users userId follows
        # and add itself to the list
        self.followMap[userId].add(userId)
        # for each user userId follows
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap: # if the user posted tweets
                index = len(self.tweetMap[followeeId]) - 1 # get the index of his last tweet
                count, tweetId = self.tweetMap[followeeId][index] # get count and tweetId
                # add to the minheap the count, tweetId, user, and decremented index
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # so now in the heap we have the list made up of all last post of each user

        while minHeap and len(res) < 10:
            # pop the most recent tweet and add it to res
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # if there are still tweets posted by that user
            # retrieve it, push it into the minheap and decrement the index
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

tw = Twitter()
print(tw.postTweet(1,5))
print(tw.getNewsFeed(1))
print(tw.follow(1,2))
print(tw.postTweet(2,6))
print(tw.getNewsFeed(1))
print(tw.unfollow(1,2))
print(tw.getNewsFeed(1))
