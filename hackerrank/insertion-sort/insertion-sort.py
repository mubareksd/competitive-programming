def insertionSort1(n, arr):
    number = arr[n - 1]
    for i in range(n - 1, -1, -1):
        if number < arr[i - 1] and i != 0:
            arr[i] = arr[i - 1]
            print(*arr)
        else:
            arr[i] = number
            print(*arr)
            break
