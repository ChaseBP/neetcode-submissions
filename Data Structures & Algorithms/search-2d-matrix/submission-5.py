class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(matrix , target, m):
            left = 0
            right = len(matrix[m]) - 1
            while left <= right:
                mid = int((left + right) / 2)

                if matrix[m][mid] == target:
                    return True
                elif matrix[m][mid] > target:
                    right = mid - 1
                elif matrix[m][mid] < target:
                    left = mid + 1
            return False
        # Iterate through row 
        for m in range(len(matrix)):
            result = binarySearch(matrix, target, m)
            
            if result == True:
                return True
        
        else:
            return False
                