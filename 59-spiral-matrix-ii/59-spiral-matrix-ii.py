class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cur = n
        itr = 1
        ret = [[0 for _ in range(n)] for _ in range(n)]
        while cur > 1:
            start = (n - cur) // 2
            end = n - 1 - start
            # up
            for i in range(start, end):
                ret[start][i] = itr
                itr += 1
            
            # right
            for i in range(start, end):
                ret[i][end] = itr
                itr += 1
                
            # down
            for i in range(end,start,-1):
                ret[end][i] = itr
                itr += 1
            
            # left
            for i in range(end, start, -1):
                ret[i][start] = itr
                itr += 1
        
            cur -= 2
        
        if cur == 1:
            ret[n // 2][n // 2] = n*n
        
        return ret
        
    
            