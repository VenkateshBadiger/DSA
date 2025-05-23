class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        k=0
        if target not in nums:
            return -1
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                k=i
                break

        nums=sorted(nums)        
        l=0
        r=n-1
        while l<=r:
            m=l+((r-l)//2) 
            real_m=(m+k)%n
            if nums[m]==target:
                return real_m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        '''
        n=len(nums)
        i=0
        def rotated(nums:List[int])-> int:
            for i in range(n-1):
                if nums[i]>nums[i+1]:
                    break 
            return i 
        k= rotated(nums)+1

        a=nums[0:k]        
        b=nums[k:n]
        nums[:]=a+b
        l=0
        r=n-1
        while l<=r:
            m=l+((r-l)//2) 
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        '''