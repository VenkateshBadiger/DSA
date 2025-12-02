from collections import Counter

MOD = 10**9 + 7
INV2 = (MOD + 1) // 2

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        #for a line to be parallel 2 of y axis should be equal 
        y_count = Counter(y for _, y in points)

        total = 0
        total_sq = 0

        for c in y_count.values():
            if c >= 2:
                a = c * (c - 1) % MOD * INV2 % MOD
                total = (total + a) % MOD
                total_sq = (total_sq + a * a) % MOD

        ans = (total * total - total_sq) % MOD
        ans = ans * INV2 % MOD
        return ans

