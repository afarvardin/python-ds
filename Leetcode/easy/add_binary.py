class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l_a = len(a)
        l_b = len(b)
        
        diff = l_a - l_b 

        if diff > 0:
            b = '0'*diff + b
        else:
            a = '0'*(diff*-1) + a

        lst_a = [int(i) for i in list(a)]
        lst_b = [int(i) for i in list(b)]

        print (lst_a, lst_b)

        sum = []

        carry = 0
        i = len(a)-1
        while i >= 0:
            local_sum = lst_a[i] + lst_b[i] + carry
            carry = 0
            if local_sum < 2:
                sum.insert(0, local_sum)
            else:
                if local_sum % 2 == 0:
                    sum.insert(0, 0)
                else:
                    sum.insert(0, 1)    
                carry = 1
            i -= 1
            
        if carry == 1:
            sum.insert(0, 1)

        return ''.join([str(x) for x in sum])
    
cls = Solution()

print(
    cls.addBinary('1', '111')
)