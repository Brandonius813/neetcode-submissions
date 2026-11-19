class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix[0]) * len(matrix)) - 1

        while l <= r:
            totalM = (l+r) // 2
            row = totalM // len(matrix[0])
            subM = totalM % len(matrix[0])

            if target > matrix[row][subM]:
                l = totalM + 1
            
            if target < matrix[row][subM]:
                r = totalM - 1
            
            if target == matrix[row][subM]:
                return True

        return False