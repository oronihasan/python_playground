Y = int(input())


def hokapoka():
    u = 0

    for i in range(1,10001):
        u += i

    for y in range(Y):
        print(u)

hokapoka()