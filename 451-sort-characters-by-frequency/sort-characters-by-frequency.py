class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sort = sorted(freq.items(), key=lambda x: x[1], reverse= True )
        result=""
        for key, value in sort:
            result += key * value
        return result
