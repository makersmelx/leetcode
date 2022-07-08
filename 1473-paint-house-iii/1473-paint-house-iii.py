class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {}
        def dfs(i, n_h, pre_color):
            if i == len(houses):
                return 0 if n_h == 0 else float('inf')
            
            if n_h < 0 or m - i < n_h:
                return float('inf')
            
            index = (i, n_h, pre_color)
            
            if index not in dp:
                if houses[i] == 0:
                    dp[index] = min([
                        dfs(i+1,n_h - (pre_color != new_color), new_color) + cost[i][new_color - 1] for new_color in range(1, n+1)]
                        )
                else:
                    dp[index] = dfs(i+1, n_h - (houses[i] != pre_color), houses[i])
            return dp[index]
        
        ret = dfs(0, target, -1)
        return ret if ret < float('inf') else -1