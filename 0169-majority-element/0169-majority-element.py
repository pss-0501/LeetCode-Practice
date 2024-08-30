class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Better Approach
        count = {}
        n = len(nums) - 1
        m = n/2
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for key, value in count.items():
            if value > m:
                return key

        return -1

        # Optimal Approach
        el = 0
        count = 0
        for i in nums:
            if count == 0:
                el = i
            if el == i:
                count += 1
            elif i != el:
                count -= 1
        
        return el
