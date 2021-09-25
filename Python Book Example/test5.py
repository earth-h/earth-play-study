from itertools import combinations #조합 사용하기 위함
import copy # 임시 links 사용하기 위함
from collections import deque

def solution(k, num, links):
    answer = 0
    
    # 간선을 -1으로 만들 조합 구해야 함(각 인덱스마다 '부모0'(왼쪽노드) 또는 '부모1'(오른쪽노드) 존재)
    link = list()

    # 간선 개수 구하기
    # link의 각 인자가 -1이 아닌 경우 개수 = 간선 개수
    linkCnt = 0
    for i in range(len(links)):
        if links[i][0] >= 0:
            linkCnt += 1
            link.append(str(i)+'0')
        if links[i][1] >= 0:
            linkCnt += 1
            link.append(str(i)+'1')

    # 간선 종류 출력
    print("간선 종류",link)

    # 간선을 제거하지 않아도 되는 경우
    if k - 1 == 0:
        for i in range(len(num)):
            answer += num[i]
        return answer

    # k는 나눌 그룹 수이므로, k-1개의 간선을 제거해서 그루핑 필요
    # 나눠진 그룹들 중 가장 큰 수가 젤 작아야 함
    if linkCnt == (k - 1):
        num.sort()
        answer = num[-1]
        return answer

    # k-1개가 간선개수와 동일하지 않다면 끊을 수 있는 가지수 모두 체크 필요
    checkList = list(map(''.join, combinations(link, k-1)))
    print(k-1,"개의 간선 조합 체크 - checkList", checkList)

    # 각 조합별로 시작
    for i in range(len(checkList)):
        tmpLinks = copy.deepcopy(links) # links 임시 복사

        #print("간선 끊기 전: ", tmpLinks)
        for j in range(len(checkList[i])):
            if j % 2 == 0:
                nodeNum = int(checkList[i][j])
                parentNum = int(checkList[i][j+1])
                tmpLinks[nodeNum][parentNum] = -1 # 간선 끊기
        # 간선 끊기 완료
        #print("간선 끊은 후: ", tmpLinks)
        nodeGroups = list() # 간선 끊은 후 그래프 그룹 만들기
        tmpVisited = [0] * len(num)

        for k in range(len(tmpLinks)):
            if tmpVisited[k] != 0: # 이미 그룹에 들어간 경우
                currentGroup = -1
                for m in range(len(nodeGroups)):
                    if k in nodeGroups[m]:
                        currentGroup = m
                if tmpLinks[k][0] != -1:
                    nodeGroups[m].append(tmpLinks[k][0])
                    tmpVisited[tmpLinks[k][0]] = 1
                if tmpLinks[k][1] != -1:
                    nodeGroups[m].append(tmpLinks[k][1])
                    tmpVisited[tmpLinks[k][1]] = 1
            else:
                if tmpLinks[k][0] == -1 and tmpLinks[k][1] == -1:
                    nodeGroups.append([k])
                    tmpVisited[k] = 1
                    continue
                else:
                    leftGroup = -1
                    rightGroup = -1
                    for m in range(len(nodeGroups)):
                        if tmpLinks[k][0] != -1 and tmpLinks[k][0] in nodeGroups[m]:
                            leftGroup = m
                        if tmpLinks[k][1] != -1 and tmpLinks[k][1] in nodeGroups[m]:
                            rightGroup = m

                    if leftGroup != -1: # 왼쪽 자식 그룹 있는 경우
                        nodeGroups[leftGroup].append(k)
                        tmpVisited[k] = 1
                        if rightGroup != -1 and leftGroup != rightGroup: # 왼쪽과 오른쪽 자식 모두 그룹이 있는데, 그룹 다르면 왼쪽에 몰기
                            for n in range(len(nodeGroups[rightGroup])):
                                nodeGroups[leftGroup].append(nodeGroups[rightGroup][n])
                            del nodeGroups[rightGroup]
                    elif rightGroup != -1:
                        nodeGroups[rightGroup].append(k)
                        tmpVisited[k] = 1
                    else:
                        if tmpLinks[k][0] != -1:
                            nodeGroups.append([k])
                            tmpVisited[k] = 1
                            nodeGroups[-1].append(tmpLinks[k][0])
                            tmpVisited[tmpLinks[k][0]] = 1
                        if tmpLinks[k][1] != -1:
                            nodeGroups.append([k])
                            tmpVisited[k] = 1
                            nodeGroups[-1].append(tmpLinks[k][1])
                            tmpVisited[tmpLinks[k][1]] = 1
           
        tmpCount = 0
        # 그룹을 지었으면 각 그룹의 합을 구하면 됨
        

        for j in range(len(nodeGroups)):
            cnt = 0
            
            for k in range(len(nodeGroups[j])):
                cnt += num[nodeGroups[j][k]]
            if tmpCount < cnt:
                tmpCount = cnt
                print("tmpCount", tmpCount)
        if answer == 0:
            answer = tmpCount
        elif answer > tmpCount:
            answer = tmpCount

        #print(nodeGroups)
    return answer


print(solution(3,[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))
#print(solution(2,[6,9,7,5],[[-1, -1], [-1, -1], [-1, 0], [2, 1]]))