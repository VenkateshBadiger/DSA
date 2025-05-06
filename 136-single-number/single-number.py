class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        uni= set(nums)
        res = 2*sum(uni) - sum_nums 
        return res
        
                         