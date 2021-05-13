class Solution:
    def minPartitions(self, n: str) -> int:
        # max function using one string parameter -> return max char value
        # 기존에 푼 방식보다 더 빠른 방식(메모리는 소량 더 사용)
        # max나 min 함수에 string 값 하나를 넣으면 해당 string 내 char 값 중 가장 크거나 작은 값 도출
        return int(max(n))

solution = Solution()
#print(solution.minPartitions("32"))
print(Solution.minPartitions(solution,"32"))