class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                if dp[j - coins[i]] != float('inf'):
                    dp[j] = min(dp[j - coins[i]] + 1, dp[j])
        
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]