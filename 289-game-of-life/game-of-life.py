class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
# Make a new matrix named old, use it to parse using directions and count the lives 
# CAUTION : Around the corners and edges the value of i,j can go negative
# After u count the lives u can start making the changes in the board  
        m = len(board)
        n = len(board[0])
        old = [row[:] for row in board]
        directions = [(-1,-1),(-1,0),(-1,1),
                      (0,-1),         (0,1),
                      (1,-1),  (1,0), (1,1)]
        for i in range(m):
            for j in range(n):
                lives = 0
                for x,y in directions:
                    ni = x + i 
                    nj = y + j
                    if 0<=ni<m and 0<=nj<n:
                        if old[ni][nj] == 1:
                            lives +=1
                    
                if  board[i][j]== 1:
                    if lives < 2 or lives > 3:
                        board[i][j] = 0
                else:
                    if lives == 3:
                        board[i][j] = 1
        return board
                
