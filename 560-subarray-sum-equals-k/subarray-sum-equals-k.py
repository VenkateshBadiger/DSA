from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case: a sum of 0 occurs once

        for num in nums:
            current_sum += num
            count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] += 1

        return count

'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        start=0
        current_sum=0

        for end in range(n):
            current_sum+=nums[end]
            while current_sum > k and start <= end:
                current_sum -= nums[start]
                start+=1
            if current_sum == k:
                count += 1
        return count
'''

'''
        count=0
        for i in range(n):
            csum=0
            for j in range(i,n):
                csum+=nums[j]
                
                if csum==k:
                    count=count+1
        return count
'''