# Spring AOP(Aspect Oriented Programming)

AOP는 Aspect Oriented Programming의 약자로 **관점 지향 프로그래밍**이라고 불립니다. 
* 관점 지향이란, 어떤 로직을 기준으로 <u>**핵심적인 관점**</u> (핵심 비즈니스 로직), <u>**부가적인 관점**</u>(핵심 로직을 실행하기 위해 행하는 데이터베이스 연결, 로깅, 파일 입출력 등)으로 나누어보고 그 관점을 기준으로 각각 모듈화하겠다는 것입니다.
* 모듈화란, 공통된 로직이나 기능을 하나의 단위로 묶는 것을 의미합니다.

AOP에서 각 관점을 기준으로 로직을 모듈화한다는 것은 코드들을 부분적으로 나누어 모듈화하겠다는 의미입니다.
이때, 소스 코드상에서 다른 부분에 <u>계속 반복해서 쓰는 코드</u> 들을 **흩어진 관심사(Crosscutting Concerns)** 라 합니다.

![AOP 예시](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile26.uf.tistory.com%2Fimage%2F994AA3335C1B8C9D28D24B)
* 위 그림처럼 <u>흩어진 관심사를 Aspect로 모듈화하고 핵심적인 비즈니스 로직에서 분리하여 재사용</u> 하겠다는 것이 AOP의 취지입니다.

## AOP 주요 개념
* Aspect: 흩어진 관심사를 모듈화한 것
  * 주로 부가기능을 모듈화함
* Target: Aspect을 적용하는 곳(클래스, 메소드 등)
* JointPoint: Advice가 적용될 위치, 끼어들 수 있는 지점