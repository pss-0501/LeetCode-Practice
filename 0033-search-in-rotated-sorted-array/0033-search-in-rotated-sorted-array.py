class Solution:
    def search(self, arr: List[int], k: int) -> int:
        low = 0
        n = len(arr)
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is the target
            if arr[mid] == k:
                return mid
            
            # Check if the left half is sorted
            if arr[low] <= arr[mid]:
                if arr[low] <= k <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, the right half must be sorted
            else:
                if arr[mid] <= k <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1