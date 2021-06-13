# mergeSort 정리
'''
* def mergeSort: mergeSort 오름차순 정렬(1차원 리스트)

* def mergeSortDouble: mergeSort 오름차순 정렬(2차원 리스트)
    - 두번째 인자로 정렬
* def mergeSortDoubleReverse: mergeSort 내림차순 정렬(2차원 리스트)
    - 두번째 인자로 정렬
'''

class Solution:
    def mergeSort(self, x: list):
        if len(x) > 1:
            mid = len(x) // 2
            lx, rx = x[:mid], x[mid:]
            self.mergeSort(lx)
            self.mergeSort(rx)

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

    def mergeSortDouble(self, x: list):
        if len(x) > 1:
            mid = len(x) // 2
            lx, rx = x[:mid], x[mid:]
            self.mergeSortDouble(lx)
            self.mergeSortDouble(rx)

            li, ri, i = 0, 0, 0
            while li < len(lx) and ri < len(rx):
                if lx[li][1] < rx[ri][1]:
                    x[i] = lx[li]
                    li += 1
                else:
                    x[i] = rx[ri]
                    ri += 1
                i += 1
            x[i:] = lx[li:] if li != len(lx) else rx[ri:]        

    def mergeSortDoubleReverse(self, x: list):
        if len(x) > 1:
            mid = len(x) // 2
            lx, rx = x[:mid], x[mid:]
            self.mergeSortDoubleReverse(lx)
            self.mergeSortDoubleReverse(rx)

            li, ri, i = 0, 0, 0
            while li < len(lx) and ri < len(rx):
                if lx[li][1] > rx[ri][1]:
                    x[i] = lx[li]
                    li += 1
                else:
                    x[i] = rx[ri]
                    ri += 1
                i += 1
            x[i:] = lx[li:] if li != len(lx) else rx[ri:]

solution = Solution()

mergeTest = [1, 2, 5, 10, 3, 4, 30]
print("before: ", mergeTest)
solution.mergeSort(mergeTest)
print("after: ", mergeTest)

mergeTestDouble = [[5,10],[2,5],[4,7],[3,9]]
print("before: ", mergeTestDouble)
solution.mergeSortDouble(mergeTestDouble)
print("after: ", mergeTestDouble)
solution.mergeSortDoubleReverse(mergeTestDouble)
print("after(Reverse): ", mergeTestDouble)
