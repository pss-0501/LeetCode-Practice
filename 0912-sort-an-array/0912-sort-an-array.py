class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(array1, array2):
            combined = []
            i = 0
            j = 0
            while i < len(array1) and j < len(array2):
                if array1[i] < array2[j]:
                    combined.append(array1[i])
                    i += 1
                else:
                    combined.append(array2[j])
                    j += 1
                    
            while i < len(array1):
                combined.append(array1[i])
                i += 1

            while j < len(array2):
                combined.append(array2[j])
                j += 1

            return combined

        if len(nums) <= 1:
            return nums
        mid_index = len(nums) // 2
        left = self.sortArray(nums[:mid_index])
        right = self.sortArray(nums[mid_index:])

        return merge(left, right)