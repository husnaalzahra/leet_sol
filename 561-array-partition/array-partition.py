from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        # Sum elements at even indices (0, 2, 4, ...)
        return sum(nums[::2])