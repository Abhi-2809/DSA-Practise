class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while(left<=right):
            # Check if the middle element is same as target
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            
            # If target is greater than middle element
            # Search on the right half so increase left pointer by 1
            elif nums[mid] < target:
                left=mid+1

            # If target is leff than middle element
            # Search on the left half so decrease right pointer by 1
            else:
                right=mid-1
        
        # Return -1 if element is not found
        return -1