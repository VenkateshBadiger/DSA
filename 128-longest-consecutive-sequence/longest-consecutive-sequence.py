class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n=len(nums)
        Max_count=0
        cur_count=0

        nums.sort()
        if n>0:
            Max_count=1
            cur_count=1
        for i in range(n-1):
            if nums[i] + 1 == nums[i+1] :
                cur_count +=1
                Max_count=max(Max_count, cur_count)
            else:
                cur_count=1
            #else:
            #    count=0  

        return Max_count