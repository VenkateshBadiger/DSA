class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums_sum=sum(nums)
        real_sum=n*(n+1) //2
        return real_sum-nums_sum