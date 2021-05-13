'''
0부터 9사이의 숫자로 이루어진 string을 입력받아서, 2진수의 합으로 나타낼 때 가장 적은 개수의 2진수로 나타낼 때의 개수 도출
>> 2진수는 0 또는 1로 나타내기 때문에, string 내 가장 큰 수의 개수만큼 더하면 된다.

예를 들어, "82734"가 인풋으로 들어오면
저 값 내에서 8이 제일 크고 8을 만들려면 1이 8번 필요하므로, 8개가 생성되어 1XXXX값이 8번 더해지면 된다.

처음에는 각 자리수의 합이 10이 넘으면 어떻게하지?라는 생각을 했지만, 각 자리수는 0에서 9사이이므로 그 걱정은 없어도 된다.
'''

class Solution:
    def minPartitions(self, n: str) -> int:
        # max function using one string parameter -> return max char value
        # 기존에 푼 방식보다 더 빠른 방식(메모리는 소량 더 사용)
        # max나 min 함수에 string 값 하나를 넣으면 해당 string 내 char 값 중 가장 크거나 작은 값 도출
        return int(max(n))

solution = Solution()
#print(solution.minPartitions("32"))
print(Solution.minPartitions(solution,"32"))