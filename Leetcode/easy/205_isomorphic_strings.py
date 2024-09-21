class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        result = {k: v for k, v in dict.fromkeys(zip(s,t))}

        tmp = {}
        for k, v in result.items():
            tmp[v] = k

        result = tmp

        list_t = list(t)
        for i, ch in enumerate(list_t):
            list_t[i] = '-' if result.get(ch) == None else result.get(ch)

        return ''.join(list_t) == s