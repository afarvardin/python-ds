def addBinary(a: str, b: str) -> str:
    # Input: a = "1010", b = "1011"
    # Output: "10101"

    if len(a) > len(b):
            larger_binary = a
            smaller_binary = b
    else:
        larger_binary = b
        smaller_binary = a

    larger_binary_len = len(larger_binary)
    smaller_binary_len = len(smaller_binary)

    extra_zeros = larger_binary_len - smaller_binary_len
    smaller_binary = '0' * extra_zeros + smaller_binary

    larger_binary = larger_binary[::-1]
    smaller_binary = smaller_binary[::-1]

    carry = 0
    sum_binary = []
    for i, n in enumerate(larger_binary):
        new_sum = carry + int(n) + int(smaller_binary[i])
        carry = 0
        if new_sum > 1:
            carry = 1
            sum_binary.append(0)
        else:
            sum_binary.append(1)

    if carry > 0:
        sum_binary.append(1)
    
    sum_binary.reverse()
    [str(x) for x in sum_binary]
    sum_two_binary = ''.join(sum_binary)
    ''.join([str(v) for v in x])
    return sum_two_binary

a = "1010"
b = "1011"
# Output: "10101"
print(addBinary(a,b))