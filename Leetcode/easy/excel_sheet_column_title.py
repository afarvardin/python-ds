class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # res = ""
        # while columnNumber > 0:
        #     columnNumber -= 1
        #     res = chr((columnNumber % 26) + ord("A")) + res
        #     columnNumber //= 26
        
        # return res
    
        AZ = {i-64: chr(i) for i in range(ord('A'), ord('Z') + 1)}

        # {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

        cn = columnNumber 
        s = ""
        while cn > 0:
            mod = (cn-1) % 26 + 1
        
            s = AZ.get(mod) + s
            cn = (cn - 1) // 26

        return s
    
cls = Solution()

# print(55, cls.convertToTitle(55))

for i in range(1,1001):
    print(i, cls.convertToTitle(i))
