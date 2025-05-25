class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
               
        
        l, r = 1, max(piles)
        
        
        while l<r:
            m=l+((r-l)//2)
            hour =0 
            for i in range(len(piles)):
                hour += math.ceil(piles[i]/m)
            if hour>h:
                l=m+1
            else:
                r=m
        return l
                



        