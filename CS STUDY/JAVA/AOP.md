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
* Advice: 실질적으로 어떤 일을 해야 하는 지(실질적인 부가기능을 담은 구현체)
* JointPoint: Advice가 적용될 위치, 끼어들 수 있는 지점
* PointCut: JointPoint의 상세 스펙을 정의한 것
  * A 메소드의 진입 시점에 호출할 것과 같이 구체적으로 Advice의 실행 지점 정의

## Spring AOP 특징
* 프록시 패턴 기반의 AOP 구현체, 프록시 객체를 쓰는 이유는 접근 제어 및 부가 기능을 추가하기 위함
* 스프링 Bean에만 AOP 적용 가능
* **모든 AOP 기능을 제공하는 것이 아닌** <u>Spring IoC와 연동하여 엔터프라이즈 어플리케이션의 가장 흔한 문제에 대한 해결책 지원</u>이 목적
  * 예를 들어, 중복 코드/프록시 클래스 작성의 번거로움/객체들 간 관계 복잡도 증가 등에 대한 해결책

## Spring AOP 사용법
### 의존성
```bash
dependencies {
    ...
    implementation 'org.springframework.boot:spring-boot-starter-aop'
}
```
### 사용법
```java
@Component
@Aspect
public class PerfAspect {

    @Around("execution(* com.earth..*.EventService.*(..))")
    public Object logPerf(ProceedingJoinPoint pjp) throws TRhrowable {
        long begin = System.currentTimeMillis();
        Object retVal = pjp.proceed(); // 메소드 호출 자체를 감쌈
        System.out.println(System.currentTimeMillis() - begin);
        return retVal;
    }
}
```
* @Around 어노테이션은 타겟 메소드를 감싸 특정 Advice를 실행한다는 의미입니다.
* 위 코드의 Advice는 타겟 메소드가 실행된 시간을 측정하기 위한 로직입니다.
* execution(* com.earth..*.EventService.*(..))의 의미는 com.earth 아래 패키지 경로의 EventService 객체의 모든 메소드에 이 Aspect을 적용하겠다는 것입니다.

### 참고 자료
* [스프링 AOP 총정리](https://engkimbs.tistory.com/746)