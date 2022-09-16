class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        if (total + target) % 2 == 1:
            return 0
        t = (total + target) // 2
        
        if t < 0:
            return 0
        
        dp = [0 for _ in range(t + 1)]
        dp[0] = 1
        
        for i in range(len(nums)):
            for j in range(t, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        
        return dp[t]