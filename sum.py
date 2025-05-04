prices = [int(input())]

quantities = [int(input())]

restriction = 3

names = [str(input())]

def whatToBuy(prices, quantities, restriction, names):
    e = sum(prices)
    o = sum(quantities) + restriction
    f = e + o
    j = [f , names]
    print(j)

whatToBuy(prices, quantities, restriction, names)