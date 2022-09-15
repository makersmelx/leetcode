class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0 for grid in row] for row in obstacleGrid]
        dp[0][0] = 1 - obstacleGrid[0][0]
        if dp[0][0] == 0:
            return 0
        for i in range(1, m):
            if obstacleGrid[i][0] == 0 and dp[i-1][0] > 0:
                dp[i][0] = 1
        
        for j in range(1, n):
            if obstacleGrid[0][j] == 0 and dp[0][j-1] > 0:
                dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]