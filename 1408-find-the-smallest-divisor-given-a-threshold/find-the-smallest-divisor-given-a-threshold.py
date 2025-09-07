class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n= len(nums)
        low, high= 1, max(nums)
        ans = high 

        while (low<= high ):
            mid =  (low+ high) // 2 
            s= sum( math.ceil(num/mid) for num in nums)

            if (s <= threshold ):
                ans = mid 
                high = mid-1
            else:
                low = mid+1
        return ans
