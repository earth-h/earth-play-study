## awk 명령어

awk는 파일로부터 레코드(record)를 선택하고, 선택된 레코드에 포함된 값을 조작하거나 데이터화하는 것을 목적으로 사용하는 프로그램입니다. 즉, awk 명령어의 입력으로 지정된 파일로부터 데이터를 분류한 뒤 분류된 텍스트 데이터를 바탕으로 패턴 매칭 여부를 검사하거나 데이터 조작 및 연산 등의 액션을 수행하고, 그 결과를 출력합니다.

## awk 명령어 예제

### 특정 필드에 대한 합 구하여 출력

`awk '{ sum += $3 } END { print "SUM: "sum }' ./test.txt`

```bash
$ cat test.txt
1 abc 30 40 50
2 def 60 70 80
3 ghi 90 10 20
awk '{ sum += $3 } END { print sum }' ./test.txt
SUM: 180
```

### 여러 필드의 값을 더한 값 출력

`awk '{ for (i=2; i≤NF; i++) total += $i }; END { print 'TOTAL: "total }' ./test.txt`

```bash
$ cat test.txt
1 abc 30 40 50
2 def 60 70 80
3 ghi 90 10 20
$ awk '{ for (i=2; i≤NF; i++) total += $i }; END { print 'TOTAL: "total }' ./test.txt
TOTAL: 450
```

### 레코드 단위로 필드 합 및 평균 값 구하기

awk '{ sum = 0 } { sum += ($3+$4+$5) } { print $0, sum, sum/3 }' ./test.txt

```bash
$ cat test.txt
1 abc 30 40 50
2 def 60 70 80
3 ghi 90 10 20
$ awk '{ sum = 0 } {sum += ($3+$4+$5) } { print $0, sum, sum/3 }' ./test.txt
1 abc    30 40 50 120 40
2 def    60 70 80 210 70
3 ghi    90 10 20 120 40
```

## 참고

### NF

NF란 현재 레코드 필드 개수를 뜻합니다.

### $i

$i란 변수 i가 매핑된 필드를 뜻합니다.

- 즉, i번째 위치 필드