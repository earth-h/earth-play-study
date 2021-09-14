# 933. Number of Recent Calls

'''
deque를 이용한 풀이
> 기존 풀이는 list였다면, deque를 이용해서 append는 오른쪽에, pop은 왼쪽으로 진행
'''
from collections import deque;

class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

ans = RecentCounter()
print([ans.ping(1), ans.ping(100), ans.ping(3001), ans.ping(3002)])