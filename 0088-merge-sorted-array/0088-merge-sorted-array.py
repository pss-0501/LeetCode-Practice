class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #a = len(nums1)
        #nums1[:n]

        for j in range(n):
            nums1[m + j] = nums2[j]

        nums1.sort()

        return nums1
        