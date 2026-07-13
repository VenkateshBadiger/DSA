class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen={}
        for i in range(n):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed],i]
            seen[nums[i]] = i