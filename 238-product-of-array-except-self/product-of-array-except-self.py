class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prev = 1
        answer = []
        for i in range(n):
            answer.append(prev)
            prev = prev * nums[i]
        
        suc = 1
        for i in range(n-1,-1,-1):
            answer[i] = answer[i]*(suc)
            suc = suc * nums[i]
        return answer
