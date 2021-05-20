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

### 생성자와 초기화

파이썬에서는 객체를 생성할 때 아래와 같이 생성자를 사용합니다.

```python
t = Test() # 생성자
```

- 생성자로 객체생성을 호출받으면, 먼저 `__new__`를 호출하여 객체를 생성할당하고, `__new__` 메소드가 `__init__` 메소드를 호출하여 객체에서 사용할 초기값들을 초기화하게 됩니다.

**[ 생성자와 초기화 예제 #1 ]**

```python
# test.py
class Test:
	def __init__(self):
		print('init')
		super().__init__()

	def __new__(cls):
		print('new')
		return super().__new__(cls)

	def number(self):
		return '123'

# test2.py
from test import Test

t = Test()

# test2.py 실행 결과
new
init
```

**[ 생성자와 초기화 예제 #2 ]**

```python
# test.py
class Test:
	def __init(self, number):
		self._number = number

	def number(self):
		return self._number

# test2.py
from test import Test

t = Test(5)

t.number()
t._number

# test2.py 실행 결과
5
5
```

- 객체 속성을 초기화합니다. `__new__` 메소드는 자동으로 실행되므로 제거합니다.
- `__init__` 메소드에 코드를 수정합니다.
- 아래의 코드에서 self._number로 할당했는데 변수명의 `_`의 의미는 다음과 같습니다.
    - 내부적으로 사용되는 변수
    - 파이썬의 기본 키워드와 충돌을 피하기 위한 변수
    - `_` 관련 네이밍컨벤션 자료
        - [https://www.python.org/dev/peps/pep-0008/#naming-conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

접근 제어자(public, private, protected)?

- Python은 기본적으로 다른 언어에 있는 접근제어자(public, private, protected)가 없습니다. 
- 즉, public이라고 봐도 무방합니다.