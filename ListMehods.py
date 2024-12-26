List1 = [1, 3, 5, 3]
List2 = [2, 4, 6]

def merge(lst1, lst2):
    for i in lst2:
        lst1.append(i)
    lst1.sort() 
    print(lst1)


merge(List1, List2)

