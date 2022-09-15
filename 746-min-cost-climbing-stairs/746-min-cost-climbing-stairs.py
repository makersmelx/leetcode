class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        if size == 2:
            return min(cost[0:2])
        first, second = cost[0], cost[1]
        for i in range(2, size):
            costs = min(first, second) + cost[i]
            first = second
            second = costs
        
        
        return min(first, second)
        