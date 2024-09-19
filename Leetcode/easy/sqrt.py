import math

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        h = x-1

        arr = range(0,x)
        mid = -1
        while l < h:
            m_idx = math.ceil((l+h)/2)
            mid = arr[m_idx]
            pow_mid = mid * mid
            if pow_mid == x:
                return mid
            elif pow_mid > x:
                h =  m_idx
            else:
                l = m_idx
                
            if l + 1 == h:
                return l

        return mid
    
cls = Solution()

print(cls.mySqrt(1023))