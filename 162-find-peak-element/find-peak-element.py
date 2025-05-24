class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        
        def get(nums, i):
            if i >= n and i < 0:
                nums[i]= -math.inf
            return nums[i] 
        
        while l<r:
            m=l+((r-l)//2)
            if nums[m]<nums[m+1]:
                l=m+1
            else:
                r=m
        return l

                