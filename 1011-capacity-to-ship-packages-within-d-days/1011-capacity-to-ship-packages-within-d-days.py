class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def CalDays(arr, cap):
            load = 0
            day = 1
            for i in arr:
                if load + i > cap:
                    day += 1
                    load = i
                else:
                    load += i
            return day       

        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2         # capacity
            d = CalDays(weights, mid)
            if d <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans