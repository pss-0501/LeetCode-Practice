class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute Force
        n = len(nums)
        d = k % n
        t = n - d
        temp = nums[t:]
        temp2 = nums[:t]
        #nums[:] = temp + temp2
        for i in range(len(temp)):
            nums[i] = temp[i]

        for j in range(len(temp2)):
            nums[len(temp) + j] = temp2[j]

        