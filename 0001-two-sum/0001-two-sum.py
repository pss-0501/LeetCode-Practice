class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for i,num in enumerate(nums):
            sub = target - num
            if sub in my_dict:
                return [my_dict[sub], i]    # return value of dict[key] & i
            my_dict[num] = i
        return[]

        