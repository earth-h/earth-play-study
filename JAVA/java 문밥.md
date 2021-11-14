# JAVA 문법

### 한 줄로 ArrayList 초기화
**[Java8 이하]**
```java
List<String> stringList = Arrays.asList("string1", "string2", "string3");
```
**[Java9 이상]**
- List.of() 추가
```java
List<String> stringList = List.of("string1", "string2", "string3");
```

**[Java10 이상]**
- var 키워드 사용
```java
var stringList = List.of("string1", "string2", "string3");
```

