class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1' and not visited[i][j]:
                visited[i][j] = True
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
        
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i,j)
                    ret += 1
        
        return ret