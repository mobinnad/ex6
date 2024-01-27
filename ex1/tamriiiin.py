#Rμν-Rgμν/2+Λgμν=8πGTμν/c⁴
def dtb(n): 
    return "{:032b}".format(int(n))
z = str(input())
ch = str(input())
n = int(input())
if __name__ == '__main__': 
    chap = str(dtb(int(ch)))
    rast = str(dtb(int(z)))
list=[]
dt = str(chap)+str(rast)
for i in range(n):
    m = int(input())
    if dt[-m-1]=='0':
        list.append('no')
    elif dt[-m-1]=='1':
        list.append('yes')
for a in range(len(list)):
    print(list[a])