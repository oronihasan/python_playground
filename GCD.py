Num1 = int(input()) #the bigger number

Num2 = int(input()) #the smaller number

def GCD(m , n):
    if n == 0:
        return m
    else: 
        return GCD(n, m % n)
    


print(GCD(Num1,Num2))