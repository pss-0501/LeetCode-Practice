class Solution(object):
    def threeSum(self, nums):
        
        target = 0
        #my_list = []
        final_list = []
        n = len(nums)

        nums.sort()

        i = 0

        for i in range(n):

            left =  i + 1
            #center = 1
            right = n - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if(sum < target):
                    left += 1

                elif(sum == target and i != left != right):          # and i != left != right
                    #my_list.append([nums[i], nums[left], nums[right]])

                    if([nums[i], nums[left], nums[right]] not in final_list):
                        final_list.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1                   
                
                else:
                    right -= 1

        return final_list