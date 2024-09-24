class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
# Runtime
# 407
# ms
# Beats
# 90.81%
# Analyze Complexity
# Memory
# 31.90
# MB
# Beats
# 86.29%
