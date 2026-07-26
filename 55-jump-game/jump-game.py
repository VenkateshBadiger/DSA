class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n =len(nums)
        maxpos = 0
        for i in range(n):
            if i > maxpos:
                return False
            maxpos = max(maxpos, i+nums[i])
        return True
