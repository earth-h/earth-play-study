# 1656. Design an Ordered Stream 

'''
기존에 풀었던 풀이보다, 메모리를 더 작게 쓰는 방법을 찾아 작성합니다.

기존에 return하는 List[str]의 경우 지역변수를 사용했는데,
아래 풀이의 경우 주어진 List를 잘라 return하는 형식으로 진행했습니다.
=> 이에 따라, 기존에 n개의 원소를 가진 List를 지역변수로 매번 호출하는 대신, int형 변수 하나만 지역변수로 쓰게 되었습니다.
'''

from typing import List

class OrderedStream:
    def __init__(self, n: int):
        self.chunkList = [""] * n
        self.ptr = 0 # chunkList의 첫 원소부터 훑기 위함
    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunkList[idKey - 1] = value

        if self.chunkList[self.ptr] == "":
            return [] # 현 위치가 비어있을 경우, 더 앞으로 나아가지 못하므로 [] return
        else:
            for i in range(self.ptr, len(self.chunkList)):
                if self.chunkList[i] == "":
                    tmpPtr = self.ptr
                    self.ptr = i
                    return self.chunkList[tmpPtr: i]
                elif i == len(self.chunkList) - 1:
                    return self.chunkList[self.ptr:]

obj = OrderedStream(5)
param_1 = list()
param_1.append(obj.insert(3, "ccccc"))
param_1.append(obj.insert(1, "aaaaa"))
param_1.append(obj.insert(2, "bbbbb"))
param_1.append(obj.insert(5, "eeeee"))
param_1.append(obj.insert(4, "ddddd"))
print(param_1)