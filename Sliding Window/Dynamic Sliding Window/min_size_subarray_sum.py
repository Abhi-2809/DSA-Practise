# Minimum size subarray - Leetcode 209
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l=0
        min_len = float('inf')
        curr=0
        for r in range(len(nums)):
            curr+=nums[r]
            while curr>=target:
                print(l,r)
                min_len = min(min_len,r-l+1)
                curr = curr - nums[l]
                l+=1
        
        return 0 if min_len==float('inf') else min_len   


