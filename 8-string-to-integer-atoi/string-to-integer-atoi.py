class Solution:
    def myAtoi(self, s: str) -> int:
        s= s.strip()
        if not s:
            return 0
        i=0
        sign = 1

        if s[i] in ["-", "+"]:
            if s[i] == "-":
                sign = -1
            i+=1
        
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result*10 + int(s[i]) 
            i += 1
        result *= sign 

        if result < -2**31:
            return -2**31
        elif result > 2**31-1:
            return 2**31-1
        
        return result

        # Simple Explaination (Venky):
        # 1. Use .strip() to remove the spaces on each side
        # 2. Check for "-" or "+" sign and store SIGN 
        # 3. Iterate through the string check if Character is a DIGIT (Stop at non character string)
        # 4. Multiply result with the Sign 
        # 5. Check if they are in the boundary

        


            
        