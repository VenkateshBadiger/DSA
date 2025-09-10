class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False 
        return goal in (s+s)
                     
"""
        new = s+s
        if goal in new:
            return True
        else:
            return False 
"""