class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        current = nums[0]
        small_inpt = nums[1:]
        small_perms = self.permute(small_inpt) 
        ans = []
        for perm in small_perms:    
            for i in range(len(perm)+1):
                ans.append(perm[0:i] + [current] + perm[i:])
        return ans