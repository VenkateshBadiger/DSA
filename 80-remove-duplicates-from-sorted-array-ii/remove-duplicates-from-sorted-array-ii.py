class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k= 0
        count = {} 
        for i in range(len(nums)):
            if count.get(nums[i],0) < 2:
                count[nums[i]] = count.get(nums[i],0) +1 
                nums[k]= nums[i]
                k+=1
        return k   
      

