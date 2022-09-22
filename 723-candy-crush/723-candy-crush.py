class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m,n = len(board), len(board[0])
        
        while True:
            stable = True
            crush = set()
            
            for i in range(m):
                for j in range(n - 2):
                    if board[i][j] == board[i][j+1] == board[i][j+2] != 0:
                        stable = False
                        for itr in range(j, n):
                            if board[i][itr] == board[i][j]:
                                crush.add((i,itr))
                            else:
                                break
            
            for i in range(m-2):
                for j in range(n):
                    if board[i][j] == board[i+1][j] == board[i+2][j] != 0:
                        stable = False
                        for itr in range(i, m):
                            if board[itr][j] == board[i][j]:
                                crush.add((itr,j))
                            else:
                                break
            if stable:
                break
            
            for x,y in crush:
                board[x][y] = 0
                
            
            for j in range(n):
                slow = m-1
                for fast in range(m-1,-1,-1):
                    if board[fast][j] != 0:
                        board[slow][j] = board[fast][j]
                        slow -= 1
                for i in range(slow, -1, -1):
                    board[i][j] = 0
            
        return board
                        