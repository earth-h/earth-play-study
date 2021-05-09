def solution(s):
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    isAlpha = False
    stringCnt = 0
    tmpStringCnt = 0
    stringLen = len(s)
    answer = 0
    
    for i in range(stringLen):
        # 알파벳이고 이미 구한 값이면 다음 루프 돌기
        if isAlpha == True:
            tmpStringCnt += 1
            if tmpStringCnt < stringCnt:
                continue
            elif tmpStringCnt == stringCnt:
                isAlpha = False
                stringCnt = 0
                tmpStringCnt = 0
                continue
            
        if s[i] >= 'a' and s[i] <= 'z':
            # 3자리 알파벳
            tmpAlpha = s[i] + s[i+1] + s[i+2]
            
            for k in range(len(alpha)): # 3자리
                if tmpAlpha == alpha[k]:
                    stringCnt = 3
                    tmpStringCnt = 1
                    isAlpha = True
                    answer = answer * 10 + k
                    break
            if isAlpha == False and i + 3 < stringLen: # 4자리
                tmpAlpha = s[i] + s[i+1] + s[i+2] + s[i+3]
                for k in range(len(alpha)):
                    if tmpAlpha == alpha[k]:
                        stringCnt = 4
                        tmpStringCnt = 1
                        isAlpha = True
                        answer = answer * 10 + k
                        break
                if isAlpha == False and i + 4 < stringLen: # 5자리
                    tmpAlpha = s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4]
                    for k in range(len(alpha)):
                        if tmpAlpha == alpha[k]:
                            stringCnt = 5
                            tmpStringCnt = 1
                            isAlpha = True
                            answer = answer * 10 + k
                            break    
        else: # 현재 숫자 들어옴
            answer = answer * 10 + int(s[i])
    
    return answer

print(solution("onefourseveneight253"))