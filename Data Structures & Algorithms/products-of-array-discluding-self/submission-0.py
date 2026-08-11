import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [1] * len(nums)
        num = nums[::-1]
        for i in range(0,len(nums)):
            if i == 0:
                left.append(1)
            else:
                product = left[i-1] * nums[i-1]
                left.append(product)
        for j in range(len(nums)-2, -1, -1):
                right[j] = nums[j+1] * right[j+1]
        res = []
        for k in range(0,len(nums)):
            value = left[k] * right[k]
            res.append(value)
        return res



        
                

        

            
            



        
            
        