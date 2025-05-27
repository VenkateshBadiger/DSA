
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            missing = arr[i] - (i + 1)
            if missing >= k:
                return k + i  # We overshot by (missing - k), so add i
        # If not returned inside loop, answer is beyond the array
        return k + len(arr)
