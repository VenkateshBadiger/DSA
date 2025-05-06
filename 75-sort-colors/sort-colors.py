class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        a=[]
        b=[]
        c=[]
        x=y=z=0
        for i in range(n):
            if nums[i]==0:
                x+=1
            elif nums[i]==1:
                y+=1
            else:
                z+=1
        a=[0]*x
        b=[1]*y
        c=[2]*z
        nums[::]=a+b+c       
       
       
       
       
       
        """ 
        for i in range(n):
            for j in range(i,n):
                   j+=1
                elif nums[i]==nums[j]:
                    i+=1
                    t= nums[i]
                    nums[i]=nums[j]
                    nums[j]=t
                else:
                    t= nums[i]
                    nums[i]=nums[j]
                    nums[j]=t
        """