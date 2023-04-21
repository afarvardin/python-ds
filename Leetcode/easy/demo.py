def is_odd(num):
    if num%2==0:
        return False
    return True

one_500 = list(range(1,500))

print(list(
    filter(is_odd, one_500)
))