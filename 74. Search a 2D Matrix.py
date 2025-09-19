class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        top, bot = 0, m - 1
        row = -1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            if target < matrix[mid][0]:
                bot = mid - 1
            else:
                top = mid + 1
        if row < 0:
            return False
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

