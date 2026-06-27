class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] == target:
                return mid

           # Searching the target 
            if nums[low] <= nums[mid]:
                # Searching in left half
                if nums[low] <= target and nums[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1   # Shifting gear to right half

            else:
                # Searching right half
                if nums[mid] < target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
                

        