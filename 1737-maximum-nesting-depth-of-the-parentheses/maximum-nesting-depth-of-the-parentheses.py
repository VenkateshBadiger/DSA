class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        max_depth = 0 
        #para= []
        for ch in s:
            if ch == "(":
                count += 1
                max_depth = max(max_depth, count)
                #para.append(count)
            elif ch == ")":
                count -= 1 
        return max_depth  
        # return max(para) if para else 0