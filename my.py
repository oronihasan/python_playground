if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    for index, i in enumerate(arr):
        for j in range(1, len(arr)):
            if i < j:
                tmp = i
                arr[index] = j
                arr[ind+1] = tmp
    
    for i in arr:
        print(i)