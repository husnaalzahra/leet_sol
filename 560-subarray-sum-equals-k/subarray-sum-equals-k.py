from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case: a prefix sum of 0 has occurred once
        
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            
            # If (curr_sum - k) exists in our map, it means we found valid subarrays
            if (curr_sum - k) in prefix_sums:
                count += prefix_sums[curr_sum - k]
                
            # Record the current prefix sum frequency
            prefix_sums[curr_sum] += 1
            
        return count