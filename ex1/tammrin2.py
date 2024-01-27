def sum(c,b):
    while b != 0:
        carryover = c & b
        c = c ^ b
        b = carryover << 1
    return c

    
n = int(input())
m = int(input())
k = int(input())
sum_n_m = sum(n,m)
print(sum_n_m)
if sum_n_m == k :
    print('YES')
else :
    print('NO')
    #end