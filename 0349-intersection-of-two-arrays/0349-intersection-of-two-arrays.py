class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) > len(nums2):
            for i in range(len(nums1)-1):
                if nums1[i] in nums2 and nums1[i] not in res:
                    res.append(nums1[i])

        else:
            for i in range(len(nums2)-1):
                if nums2[i] in nums1 and nums2[i] not in res:
                    res.append(nums2[i])

        return res


