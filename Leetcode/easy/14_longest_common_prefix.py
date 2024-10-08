class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        results = [set(tup) for tup in zip(*strs)]

        c = ''
        for x in results:
            if len(x) == 1:
                c += x.pop()
            else:
                break
        
        return c 