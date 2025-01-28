class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        final = []

        n = len(nums)
        nums.sort()

        i = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1

            while left < right:
                sum1 = nums[i] + nums[left] + nums[right]
                if sum1 < target:
                    left += 1

                elif sum1 > target:
                    right -= 1
                
                else :
                    final.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

        return final

