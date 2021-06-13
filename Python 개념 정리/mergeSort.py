# 기본 mergeSort

def mergeSort(x: list):
    if len(x) > 1:
        mid = len(x) // 2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]

mergeTest = [1, 2, 5, 10, 3, 4, 30]
print("before: ", mergeTest)
mergeSort(mergeTest)
print("after: ", mergeTest)
    