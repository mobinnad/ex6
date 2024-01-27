def sum_of_divisors(n):
    s = 0
    for i in range (1, n+1):
        if n % i == 0:
            s += i
    return s

def base_conversion(n, base):
    digits = []
    result = 0
    while n:
        n, remainder = divmod(n, base)
        digits.append(str(remainder))
    for i in range (len(digits)):
        result += int(digits[len(digits)- i - 1]) * (10 ** (len(digits) - i - 1))
    return result

total_sum = 0
invalid_bases = 0
num, base = map(int,input().split( ))
while(num != -1 & base != -1):
    if 2 <= base <= 9:
        num = sum_of_divisors(num)
        total_sum += base_conversion(num, base)
    else:
        invalid_bases += 1
    num, base = map(int, input().split())
if invalid_bases != 0:
    print("invalid base!")
else:
    print(total_sum)