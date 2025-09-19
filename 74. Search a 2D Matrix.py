class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col=len(matrix), len(matrix[0])
        for i in range(row):
            if matrix[i][0]<=target<=matrix[i][col-1]:
                for j in range(col):
                    if matrix[i][j]==target:
                        return True
                return False
            else:
                continue
        return False