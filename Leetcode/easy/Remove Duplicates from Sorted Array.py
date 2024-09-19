class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        non_repeat_id = 0
        len_nums = len(nums)
        for i in range(1, len_nums):
            if nums[i] != nums[non_repeat_id]:
                nums[non_repeat_id+1] = nums[i]
                non_repeat_id += 1
        
        print(nums)
        return non_repeat_id + 1

    

    
a = [-1,-1,0,0,1,1,1,2,2,3,3,4]
cls=Solution()

print(
    cls.removeDuplicates(a)
)
