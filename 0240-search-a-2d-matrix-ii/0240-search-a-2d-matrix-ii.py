class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # BF O n**2
        # Better Solution
        def BS(arr, k):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == k:
                    return mid
                elif arr[mid] < k:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            index = BS(matrix[i], target)
            if index != -1:
                return True
        return False