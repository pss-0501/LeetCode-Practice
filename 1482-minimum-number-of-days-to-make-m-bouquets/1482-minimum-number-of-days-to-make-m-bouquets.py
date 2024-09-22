class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def CountDays(arr, i):
            bou = 0
            count = 0
            for a in arr:
                if a <= i:
                    count += 1
                    if count == k:
                        bou += 1
                        count = 0
                else:
                    count = 0

            return bou

        if len(bloomDay) < m * k:
            return -1

        low = 1
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            BouReady = CountDays(bloomDay, mid)
            if BouReady >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
