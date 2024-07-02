class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        counts = {}
        for num in nums1:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        res = []
        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        return res
