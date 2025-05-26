class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        import math
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def compute_sum(divisor):
            return sum(math.ceil(num / divisor) for num in nums)
        
        left, right = 1, max(nums)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            current_sum = compute_sum(mid)
            
            if current_sum <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
