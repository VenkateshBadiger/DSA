class Solution:
    def maxDepth(self, s: str) -> int:
        count=0 
        para= []
        for ch in s:
            if ch == "(":
                count += 1
                para.append(count)
            elif ch == ")":
                count -= 1 
            
        return max(para) if para else 0