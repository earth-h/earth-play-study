def solution(places):
    answer = []
    
    for i in range(len(places)):
        # places[i]가 이번에 체크할 대기실
        print("i ",i)
        place = list()
        print(len(place))
        for j in range(len(places[i])):
            print("j ",j)
            row = places[i][j]
            for k in range(len(places[i][j])):
                print("k ", k)
                print(places[i][j][k])
                place[j].append(places[i][j][k])
                
        print(place)
    '''
    # 거리두기 잘되는 경우
    answer.append(1)
    # 거리두기 안되는 경우
    answer.append(0)
    '''
    return answer

# 맨해튼 거리 반환
def checkDistance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2) 

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))