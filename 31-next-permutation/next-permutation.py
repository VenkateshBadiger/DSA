class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        i = n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1

        if i>=0:
            j=n-1
            while nums[j] <= nums[i]:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right]=nums[right], nums[left]
            left += 1
            right -= 1
        
        
        
        
        
        
        
        
        
        '''
        def Rearrange(a):
            if a <= 0:
                nums.reverse()
                return
            
            if nums[a]>nums[a-1]:
                switch(a)
            
            else:
                sub(a)

        def switch(b):
            x=nums[b]
            nums[b]=nums[b-1]
            nums[b-1]=x

        def sub(c):
            c=c-1
            Rearrange(c)
        
        Rearrange(n-1)
        '''