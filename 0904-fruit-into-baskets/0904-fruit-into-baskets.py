class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        left = 0
        maxLen = 0
        n = len(arr)
        count = {}      # fruit, num
        for right in range(n):
            count[arr[right]] = count.get(arr[right], 0) + 1
 
            while len(count) > 2:
                count[arr[left]] -= 1
                if count[arr[left]] == 0:
                    del count[arr[left]]
                left += 1
                
            maxLen = max(right - left + 1, maxLen)
                
        return maxLen