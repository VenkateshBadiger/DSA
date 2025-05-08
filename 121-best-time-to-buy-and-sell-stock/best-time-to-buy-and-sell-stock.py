class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ele =float('inf')
        max_ele = 0
        for price in prices:
            min_ele=min(min_ele,price)
            max_ele=max(max_ele,price-min_ele)

        return max_ele

        
        
        '''
        n=len(prices)
        min_index=prices.index(min(prices))
        if min_index < n-1:
            sub=prices[min_index:]
            max_sub_ele=max(sub)
            return max_sub_ele-prices[min_index]
        
        else:
            return 0
        '''
        
        #for i in range(n):
        #    for j in range(n):
                 