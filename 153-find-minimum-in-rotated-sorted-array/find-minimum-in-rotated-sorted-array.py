class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        k=0
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                k=i
        return nums[k]
        '''l,r = 0,n-1
        target=min(nums)
        while l<=r:
            m=l+((r-l)//2)
            real_m=(n+k)%n
            if nums[real_m]==nums[target]:
                return m
            elif nums[real_m]<nums[target]:
                l=m+1
            else:
                r=m-1
            '''