c=int(input())
d=int(input())
m=0
x=bin(c^d)[:]
for i in range(len(x)):
    if x[i] == "1":
    	m+=1
print(m)

    	