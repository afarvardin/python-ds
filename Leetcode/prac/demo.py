class Solution:
    
    def romanToInt(self, s: str) -> int:
        romanInitials = {
            "I": 1, 
            "IV": 4,
            "V" : 5, 
            "IX": 9,
            "X" : 10, 
            "XL": 40,
            "L" : 50, 
            "XC": 90,
            "C" : 100, 
            "CD": 400,
            "D" : 500, 
            "CM": 900,
            "M" : 1000,
            }

        lst_roman = list()
        lst_roman.extend(s)
        
        lst_kv_tuple = []
        tmp = ""
        count = 0
        given_nunmber = len(lst_roman)
        for idx,n in enumerate(lst_roman):
            if tmp == "":
                count +=1
                tmp = n
            elif tmp == n:
                count +=1
            elif tmp != n:
                lst_kv_tuple.append( (tmp,count) )
                tmp = n
                count = 1

            if(given_nunmber == idx+1):
                lst_kv_tuple.append( (tmp,count) )

        print(lst_kv_tuple)
        for t in lst_kv_tuple:
            print( [romanInitials[t[0]] for i in range(t[1])] )

        return 10
            


obj = Solution()
# print(obj.romanInitials)
print( obj.romanToInt("LVIII") )