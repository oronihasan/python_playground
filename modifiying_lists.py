list = ['a', 'b', 'c']
index = int(input())
new_element = input()

#def change_element(lst, index, new_element):
    #list[index] = new_element
    #print(list)
    
def change_element(lst, index, new_element):
    index = int(index)
    lst[index] = new_element
    print(lst)

change_element(list, index, new_element)



