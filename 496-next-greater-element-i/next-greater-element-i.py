class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greatest = {}
        for num in nums2:
            while stack and num > stack[-1]:
                next_greatest[stack.pop()] = num
            stack.append(num)
        return [next_greatest.get(n,-1) for n in nums1]


        '''
        ans = []
        for num in nums1:
            idx= nums2.index(num)
            next_greater=-1
            
            for j in range(idx+1, len(nums2)):
                if num < nums2[j]:                    
                    next_greater = nums2[j]
                    break
            ans.append(next_greater)
                
        return ans
        '''