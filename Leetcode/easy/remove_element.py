class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        len_nums = len(nums)

        if len_nums == 0:
            return 0

        idx = -1
        c = 0
        for i in range(len_nums):
            if nums[i] != val:
                idx += 1
                nums[idx] = nums[i]
        return idx+1
    
cls = Solution()

nums = [0,1,2,2,3,0,4,2]
val = 2

print(cls.removeElement(nums, val))