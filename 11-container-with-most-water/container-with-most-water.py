class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        max_area=0
        i,j = 0, len(height)-1

        while(i<j):
            area = min(height[i], height[j])* (j-i)
            max_area= max(max_area, area)
            if height[i]<height[j]:
                i=i+1
                
            else: 
                j=j-1
        return max_area




        #for i in range(n):
        #    b1=height[i]
        #    for j in range(i+1,n):
        #        b2=height[j]
        #        area=min(b1,b2)*(j-i) 
        #        max_area=max(max_area, area)
        #return max_area