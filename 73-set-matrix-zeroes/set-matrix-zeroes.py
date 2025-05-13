class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        zeros=[]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    zeros.append((i,j))
                    

        def make(a,b):
            matrix[a] = [0]*c
            for i in range(r):
                matrix[i][b]=0


        for a,b in zeros:
            make(a,b)