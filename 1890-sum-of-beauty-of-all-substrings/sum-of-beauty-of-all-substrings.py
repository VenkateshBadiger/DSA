class Solution:
    def beautySum(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            freq = Counter()
            for j in range(i, len(s)):
                freq[s[j]] += 1
                beauty = max(freq.values()) - min(freq.values())
                result += beauty
        return result