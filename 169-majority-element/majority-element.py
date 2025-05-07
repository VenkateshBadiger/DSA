class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)
        nums.sort()

        return nums[n//2]
        #as it is the major element it will be in the middle 
        #after sorting as it is the number that appears more than n/2 times 


        '''
        count={}
        for n in nums:
            count[n]= count.get(n,0)+1
        max_element=max(count,key=count.get)
        return max_element
        '''