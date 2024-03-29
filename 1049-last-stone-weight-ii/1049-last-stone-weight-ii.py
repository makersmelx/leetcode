class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        total = sum(stones)
        target = total // 2
        
        dp = [0 for _ in range(target + 1)]
        
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        
        return total - 2 * dp[target]