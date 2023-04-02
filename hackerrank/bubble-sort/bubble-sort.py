def countSwaps(a):
    ret = [0, 0, 0]
    n = len(a)
    for i in range(0, n):
        for j in range(0, n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                ret[0] += 1
    ret[1] = a[0]
    ret[2] = a[-1]
    print("Array is sorted in {} swaps.".format(ret[0]))
    print("First Element: {}".format(ret[1]))
    print("Last Element: {}".format(ret[2]))
