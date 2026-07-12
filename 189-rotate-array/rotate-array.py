class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        a = nums[n-k:]
        b = nums[0:n-k]
        nums[:] = a + b 