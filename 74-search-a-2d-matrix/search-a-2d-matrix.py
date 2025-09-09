class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols= len(matrix), len(matrix[0])
        n =  rows * cols-1
        l, r= 0,n
        
        while l<=r:
            m= (l+r)//2
            row, col= divmod(m, cols) 
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                r = m-1
            else:
                l= m+1
        return False 