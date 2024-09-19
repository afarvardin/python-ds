class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for ch in s.lower():
            if ch.isalpha() or ch.isnumeric():
                new_s += ch
        return  new_s == new_s[::-1]