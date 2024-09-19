# import math
# import time

# class Solution:

#     def intToRoman(self, num: int) -> str:
#         num_arr = self.divide_number(num)
        
#         # print(f"divide_number {num} : {num_arr}") 

#         roman = ""
#         coef = 1
#         for n in num_arr:
#             if n == 0:
#                 coef *= 10
#                 continue
            
#             if n in self.symbols.keys():
#                 roman = self.symbols[n] + roman 
#             else:
#                 roman = self.asssemble_symbols(n, coef) + roman

#             coef *= 10

#         return roman

#     symbols = {
#         1   : "I" ,
#         5   : "V" ,
#         10  : "X" ,
#         50  : "L" ,
#         100 : "C" ,
#         500 : "D" ,
#         1000: "M" ,
#         4   : "IV",
#         9   : "IX",
#         40  : "XL",
#         90  : "XC",
#         400 : "CD",
#         900 : "CM"
#     }

#     def divide_number(self, num: int) -> list:
#         s = time.time()
#         lst=[]
#         coef = 1
#         # "12"
#         # "21"
#         for ch in str(num)[::-1]:
#             lst.append(int(ch) * coef)
#             coef *= 10
        
#         print("divide_num time: ", time.time() - s)
#         return lst
    
#         # temp_num = num
#         # sep_num = []
#         # coef = 1
#         # while(temp_num > 0):
#         #     tmp = int(temp_num%10) 
#         #     sep_num.append(tmp * coef)
#         #     temp_num = math.floor(temp_num / 10)
#         #     coef *= 10
        

#     def asssemble_symbols(self, n, coef) -> str:
#         s = time.time()
#         local_roman = ""
        
#         n = int(n / coef)

#         if n > 1 and n < 4:
#             local_roman = self.symbols[coef] * n
#         else:
#             rn = 5*coef
#             local_roman = self.symbols[rn] + (self.symbols[coef] * (n-5))
            
#         print(f"assembly time {n}: ", time.time() - s)
#         return local_roman


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000,  900, 500, 400,  100,  90,  50,  40,   10,   9,    5,   4,   1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        roman = []
        for i, value in enumerate(values):
            while num >= value:
                num -= value
                roman.append(symbols[i])
        
        return ''.join(roman)


solution = Solution()
# # # for i in range(1,101):
# # #     print(f"{i}   => {solution.intToRoman(i)} \n")

i = 3749
print(f"{i}   => {solution.intToRoman(i)}")
