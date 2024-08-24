class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Brute Force
        for i in range(len(nums)):
            found_duplicate = False
            
            # Compare the current element with every other element in the array
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    found_duplicate = True
                    break
            
            # If no duplicate is found, return the current element
            if not found_duplicate:
                return nums[i]

        # Better Solution
        mydict = {}
        for i in range(len(nums)):
            if nums[i] in mydict:
                mydict[nums[i]] += 1
            else:
                mydict[nums[i]] = 1

        for key, value in mydict.items():
            if value == 1:
                return key

        return 0