class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        count =1
        for i in range(n-1):
            if nums[i+1]!=nums[i]:
                nums[count]=nums[i+1]
                count += 1
                
        return count 