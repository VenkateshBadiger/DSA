class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n= len(nums)
        stack = []
        ans = [-1]*n
        for i in range(2* n-1, -1, -1):
            current = nums[i % n]
            while stack and stack [-1]<= current:
                stack.pop()
            if stack and i<n:
                ans[i] = stack[-1]
            stack.append(current)
        return ans