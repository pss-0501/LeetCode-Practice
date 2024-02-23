class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans=[]

        for i in nums1:
            start = 0
            end = len(nums2)-1
            while start <= end:
                mid = (start + end)//2
                if nums2[mid] == i and nums2[mid] not in ans:
                    ans.append(nums2[mid])
                    break
                elif i<nums2[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return ans

