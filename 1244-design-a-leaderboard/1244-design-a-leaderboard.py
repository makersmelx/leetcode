class Leaderboard:

    def __init__(self):
        self.data = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.data[playerId] += score

    def top(self, K: int) -> int:
        return sum(heapq.nlargest(K, self.data.values()))

    def reset(self, playerId: int) -> None:
        self.data[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)