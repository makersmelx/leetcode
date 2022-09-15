class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        if size == 2:
            return min(cost[0:2])
        first, second = 0, 0
        for i in range(2, size + 1):
            costs = min(first + cost[i-2], second + cost[i-1])
            first = second
            second = costs
        
        
        return second
        