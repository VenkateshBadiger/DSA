class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        citations.sort(reverse=True)
        h = n
        while h>0:
            count = 0 
            for i in range(n):
                if h <= citations[i]:
                    count += 1
            if h <= count:
                return h
            else:
                 h -= 1 

        return h