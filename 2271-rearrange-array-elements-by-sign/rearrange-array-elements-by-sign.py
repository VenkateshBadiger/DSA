class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
        for i in range(len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
        j=0
        k=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=pos[j]
                j+=1
            else:
                nums[i]=neg[k]
                k+=1 
        return nums     
        
        
        #for i in range(len(nums)):
        #   for j in range(len(nums)):
        #       if nums[i]>0 and i%2==1 and nums[j]<0 and j%2==0:
        #            temp = nums[j]
        #            nums[j]=nums[i]
        #            nums[i]=temp
                #elif nums[i]>0 and i%2==0 and nums[j]>0 and j%2==1:
        return nums
                

