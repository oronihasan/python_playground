iterations = int(input())
num1 = int(input())
num2 = int(input())

def bigger(arg1, arg2):
    if arg1 > arg2:
        big = arg1
    else:
        big = arg2
    return big
        
for i in range(iterations):
    
    if num1 < 2 or num2 < 2:
        break

    k = bigger(num1 , num2)
    
    if k == num1:
        num1 /= 2
        print(num1)
    else:
        num2 /= 2
        print(num2)
    