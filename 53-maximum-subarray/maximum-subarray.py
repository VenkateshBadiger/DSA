class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
        
        
        '''
        n=len(nums)
        left=nums[:n//2]
        right=nums[n//2:]

        left_sum=sum(left)
        right_sum=sum(right)

        max_sum=max(max_sum,left_sum,right_sum)
        '''