# 1282. Group the People Given the Group SIze They Belong To

'''
기존 코드의 경우 메모리 사용량이나 실행 시간이 오래 걸려서 discussion 참조하여 수정
> dictionary를 사용하므로써, 기존보다 메모리 덜 씀(list로 풀때는 []와 같이 빈 list가 존재해서 좀 더 썼음)
'''

from typing import List

class Solution:
    '''
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sortedGroupSizes = sorted(groupSizes, reverse=True)
        # tmpList[index] => (people count == index) group
        tmpList = [[] for _ in range(sortedGroupSizes[0])]
        ansList = list()
        
        for person in range(len(groupSizes)):
            # grouping
            if tmpList[groupSizes[person] - 1] == [] or len(tmpList[groupSizes[person] -1][-1]) >= groupSizes[person]:
                tmpList[groupSizes[person] - 1].append([person])
            else:
                tmpList[groupSizes[person] - 1][-1].append(person)
            
            # make answer List
            if len(tmpList[groupSizes[person] - 1][-1]) == groupSizes[person]:
                    ansList.append(tmpList[groupSizes[person] -1][-1])
                    
        return ansList
    '''
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupDict = dict()
        ansList = list()
        for person in range(len(groupSizes)):
            # groupSizes[person]명 그룹이 이미 groupDict에 존재
            numOfPeople = groupSizes[person]
            if numOfPeople in groupDict:
                if len(groupDict[numOfPeople][-1]) < numOfPeople:
                    groupDict[numOfPeople][-1].append(person)
                else:
                    groupDict[numOfPeople].append([person])
            else:
                groupDict[numOfPeople] = [[person]]
            if len(groupDict[numOfPeople][-1]) == numOfPeople:
                ansList.append(groupDict[numOfPeople][-1])
        return ansList

solution = Solution()
print("answer:",solution.groupThePeople([3,3,3,3,3,1,3]))