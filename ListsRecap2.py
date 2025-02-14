list1 = [2, 5, 7]
list2 = [4, 5, 8]


def reverse2(lst2):
    re_list = []
    for i in range(len(lst2)):
        re_list.append(lst2)
    print(re_list)

reverse2(list2)

def reverse(lst):
    ReList = []

    real_len = len(lst) - 1
    i = 0
    for val in lst:
        ReList.append(lst[real_len - i])
        i = i + 1
        
    print(ReList)

reverse(list1)