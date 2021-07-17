# 1281. Subtract the Product and Sum of Digits of an Integer

'''
n으로 주어진 숫자를 각 자리수로 나눌 때, n을 string으로 변환했다가 int로 변환하는 작업을 거쳤다.
이 방법이 아닌, 해당 숫자를 10으로 나눠가면 나머지 값이 각 자리의 수가 되므로 해당 로직으로 변경해보았다.
'''

class Solution:
    def subtractProductAndSum(selfl, n: int) -> int:
        p, s = 1, 0

        while n > 0:
            n, digit = divmod(n, 10) # 10으로 나눈 나머지는 digit에, 몫은 n에
            p *= digit
            s += digit
        
        return p - s

ans = Solution()
print(ans.subtractProductAndSum(124))