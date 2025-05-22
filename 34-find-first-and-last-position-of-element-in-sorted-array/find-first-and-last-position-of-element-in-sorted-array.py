from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def FindBound(isFirst):
            n = len(nums)
            l = 0
            r = n - 1
            bound = -1

            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    bound = m
                    if isFirst:
                        r = m - 1
                    else:
                        l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            return bound

        start = FindBound(True)
        end = FindBound(False)
        return [start, end]
