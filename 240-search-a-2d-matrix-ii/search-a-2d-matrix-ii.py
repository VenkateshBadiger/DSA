class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols =  len(matrix), len(matrix[0])
        row , col = 0, cols - 1        #(Top right) coordinates of the element we are starting 
        while row < rows and col>=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]< target:
                row =  row + 1
            else:
                col= col -1
        return False
     