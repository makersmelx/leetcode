class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2
        
        dp = [[0 for _ in range(target + 1)] for _ in nums]
        
        for j in range(nums[0], target + 1):
            dp[0][j] = nums[0]
        
        for i in range(len(nums)):
            for j in range(1, target+1):
                if j >= nums[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - nums[i]] + nums[i])
                else:
                    dp[i][j] = dp[i-1][j]
        
        
        for i in range(len(nums)):
            if dp[i][target] == target:
                return True
        
        return False
            