class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
        
        # if nums[i] > target:
        #     return i
        return len(nums)