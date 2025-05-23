class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        k=0
        if target not in nums:
            return False

        for i in range(1,n):
            if nums[i-1]>nums[i]:
                k=i
        l, r = 0, n-1
        while l<=r:
            m=l+((r-l)//2)
            real_m=(m+k)%n
            if nums[real_m]== target:
                return True
            elif nums[real_m]< target:
                l=m+1
            else:
                r=m-1