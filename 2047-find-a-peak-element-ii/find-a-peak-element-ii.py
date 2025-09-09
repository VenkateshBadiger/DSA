class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows,  cols = len(mat), len(mat[0])
        left, right = 0, cols-1

        while left <=  right:
            mid =  (left + right) // 2

            max_row=0
            for i in range(rows):
                if mat[i][mid] > mat[max_row][mid]:          
                    max_row= i
            left_value= mat[max_row][mid-1] if mid -1 >= 0 else -1 
            right_value= mat[max_row][mid+1] if mid +1 <cols else -1
            value = mat[max_row][mid]
            if value> left_value and value> right_value:
                return [max_row, mid]
            elif value < left_value :
                right = mid -1
            else:
                left = mid +1
