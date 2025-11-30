class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        if need == 0:
            return 0
        
        prefix = 0
        seen = {0: -1}  # prefix mod → index
        result = len(nums)
        
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - need) % p
            
            if target in seen:
                result = min(result, i - seen[target])
            
            seen[prefix] = i
        
        return result if result < len(nums) else -1
