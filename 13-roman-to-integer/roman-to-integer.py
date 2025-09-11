class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        # simple explaination :
        # 1. Make a hash map  2. Iterate left too right check if the first element is smaller than the second if yes then subtract it from the second and add it to the result and  
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000 
            }
        i=0
        while i < len(s):
            
            if i+1 < len(s) and  map[s[i]] < map[s[i+1]] :
                result += map[s[i+1]] - map[s[i]]
                i += 2
            else:
                result += map[s[i]]
                i+=1
        return result 
