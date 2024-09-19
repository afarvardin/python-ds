class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {')':'(', '}':'{', ']':'['}
        stack = []

        for ch in s:
            if ch in p_map:
                top_elem = stack.pop() if stack else None
                if p_map[ch] != top_elem:
                    return False
            else:
                stack.append(ch)
        
        return not stack
