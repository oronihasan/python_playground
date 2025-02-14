n = int(input())

#rows = int(n/2)+2
for i in range(n):
    k = i+1
    if  k % 2 == 1:
        print(k * '*')
    # if i / 2 == 1:
    #     print(i * '*')
