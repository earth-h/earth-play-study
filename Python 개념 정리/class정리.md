### Python 클래스 기본 정리

# 클래스

- 클래스는 객체의 구조와 행동을 정의합니다.
- 객체의 클래스는 초기화를 통해 제어합니다.
- 클래스는 복잡한 문제를 다루기 쉽도록 만듭니다.

## 클래스 정의

- 클래스를 작성하기 위해서는 class 키워드를 사용하여 새로운 클래스를 작성합니다.
- Python의 대부분 네이밍컨벤션이 단어와 단어 사이에 _를 넣는다면, 클래스의 네이밍컨벤션은 CamelCase를 사용합니다.

```python
class makeClass:
	def __init__(self, param):
		...
```

### 클래스 사용해보기

```python
# test.py
class Test:
	pass

# test2.py
from test import Test

Test
t = Test() # 객체 생성 시 new 키워드 사용하지 않음
type(t)

# test2.py 실행 결과
<class 'test.Test'>
<class 'test.Test'>
```

- 객체 생성 시 new 키워드를 사용하지 않습니다.

```python
# test.py
class Test:
	def number(self):
		return '123'

# test2.py
from test import Test

t = Test()
t.number()
Test.number(t)

# test2.py 실행 결과
'123'
'123'
```

- Python 메소드의 첫번째 파라미터명은 관례적으로 self라는 이름을 사용합니다.
- 호출 시 **호출한 객체 자신이 전달**되기 때문에 `self`라는 이름을 사용하며, **클래스에서 바로 메소드로 접근하면서 객체를 파라미터로 전달해도 동일한 결과값**을 얻을 수 있습니다.