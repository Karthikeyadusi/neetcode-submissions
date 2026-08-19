class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        total = 0
        for num in nums:
            total+=num
            if max_sum < total:
                max_sum = total
            if total<0:
                total = 0
        return max_sum
        