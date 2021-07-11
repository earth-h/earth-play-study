# 1108. Defanging an IP Address

'''
SIMPLE SOLUTION using join

- 문자열 나누기 :: split() 함수
파이쎤에서 문자열을 쪼개는 함수로, 파라미터로 구분자를 주면 해당 구분자를 기준으로 문자열을 잘라 리스트 형식으로 반환
(파라미터가 주어지지 않으면 공백을 기준으로 문자 나눔)

- 문자열 합치기 :: join() 함수
join 함수는 리스트의 문자열들을 합치는 역할

예시) 리스트들 사이에 아무것도 넣지 않고 합칠 경우("".join(리스트))
str = "Hello my name is earth"
split_str = str.split()
print(split_str) #['Hello', 'my', 'name', 'is', 'earth']
join_str = "".join(split_str)
print(join_str) #Hellomynameisearth

예시) 리스트들 사이에 특정 파라미터를 넣고 합칠 경우("특정 문자열".join(리스트))
str = "Hello my name is earth"
split_str = str.split()
print(split_str) # ['Hello', 'my', 'name', 'is', 'earth']
join_str = "-".join(split_str)
print(join_str) # Hello-my-name-is-earth

'''

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split('.'))

answer = Solution()
print(answer.defangIPaddr("1.1.1.1"))