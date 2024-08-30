class Solution:
    def majorityElement(self, nums: List[int]) -> int:
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