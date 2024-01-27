import math

operation = input()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
def lcm_of_list(numbers):
    lcm_result = numbers[0]
    for number in numbers[1:]:
        lcm_result = lcm(lcm_result, number)
    return lcm_result

operation = operation.lower()

flist = []
while True:
	f = input()
	if f == "end":
		break
	else:
		flist.append(int(f))

if operation == "sum":
    numbers = flist
    result = sum(numbers)
    print(result)
elif operation == "max":
    numbers = flist
    result = max(numbers)
    print(result)
elif operation == "min":
    numbers = flist
    result = min(numbers)
    print(result)
elif operation == "average":
    numbers = flist
    result = sum(numbers) / len(numbers)
    print(result)
elif operation == "lcd":
    numbers = flist
    result = lcm_of_list(numbers)
    print(result)
elif operation == "gcd":
    result = flist[0]
    for m in flist[1:]:
    	result = math.gcd(result, m)
    print(result)
else:
    print("Invalid command")