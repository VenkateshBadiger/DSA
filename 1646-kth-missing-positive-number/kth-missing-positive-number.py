class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss= []
        i=0
        num=1
        while len(miss)< k :
            if i<len(arr) and arr[i] == num :
                i+=1
            else: 
                miss.append(num)
            num += 1
        return miss[-1]