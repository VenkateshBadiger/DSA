class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        ser=[0,1]
        for i in range(2,n+1):
            ser.append(ser[i-1]+ser[i-2])
        return ser[n]
