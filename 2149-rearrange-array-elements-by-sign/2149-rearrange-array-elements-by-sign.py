class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        poslist = []
        neglist = []
        result = []

        for num in nums:
            if num < 0:
                neglist.append(num)
            else:
                poslist.append(num)
        
        
        for i in range(len(nums)//2):
            result.append(poslist[i])
            result.append(neglist[i])
        return result