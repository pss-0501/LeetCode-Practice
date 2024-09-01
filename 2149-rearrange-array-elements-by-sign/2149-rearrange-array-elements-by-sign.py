class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            elif nums[i] < 0:
                neg.append(nums[i])

        n = len(nums) // 2
        nums = []

        for i in range(n):
            # if i % 2 ==0:
            nums.append(pos[i])
            # else:
            nums.append(neg[i])

        return nums