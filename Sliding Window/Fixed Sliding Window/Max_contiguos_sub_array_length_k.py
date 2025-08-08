class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        max_sum = sum(nums[:k])

        window_sum = max_sum

        for i in range(len(nums)-k):
            window_sum = window_sum + nums[i+k] - nums[i]
            max_sum = max(window_sum,max_sum)
    
        return max_sum