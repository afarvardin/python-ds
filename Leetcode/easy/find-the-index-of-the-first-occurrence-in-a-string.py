class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l_h = len(haystack)
        l_n = len(needle)

        # abSADbutsad
        # SAD

        for i in range(l_h):
            if haystack[i:i+l_n] == needle:
                return i
        
        return -1
