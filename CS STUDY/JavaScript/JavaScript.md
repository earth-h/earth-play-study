## 호이스팅
컴파일 단계 동안, 코드가 실행되기 마이크로 초 전, 함수와 변수 선언이 스캔됩니다. 모든 함수와 변수 선언들은 lexical 환경이라 불리는 자바스크립트 데이터 구조 내의 메모리에 추가됩니다. 그리고 소스 코드 내 실제 선언되기 전일지라도 사용할 수 있게 됩니다.

이러한 일련 과정을 **호이스팅**이라고 합니다.

### lexical 환경이란 무엇일까?
lexical 환경은 identifier - value 매핑 데이터 구조를 의미합니다.
* identifier(식별자): 변수/함수의 이름을 참조
* value(변수/함수명): 실제 객체(포함된 함수 객체) 또는 원시값을 참조

```javascript
LexicalEnvironment = {
    Identifier: <value>,
    Identifier: <function object>
}
```

즉 lexical 환경은 프로그램이 실행되는 동안 변수와 함수가 존재하는 장소입니다.

### 호이스팅 함수 선언

```javascript
helloWorld()
function helloWorld() {
    console.log('Hello World!')
}
```
컴파일 단계에서 함수 선언이 메모리에 추가된다는 것을 알고 있기 때문에 위와 같이 실제 함수 선언 전 우리는 코드로 해당 선언을 접근할 수 있습니다.

이 경우, lexical 환경은 아래와 같습니다.
```javascript
lexicalEnvironment = {
    helloWorld: < func >
}
```
* 자바스크립트 엔진이 helloWorld() 호출을 접하게 되면 lexical 환경 내부를 살펴보고, 함수를 찾은 후 실행 시킬 수 있게 됩니다.

### 함수 표현식 호이스팅
오직 함수 선언부만이 자바스크립트 내부에서 호이스트되고, 함수 표현식은 호이스트되지 않습니다. 

예를 들어, 아래 코드는 동작하지 않습니다.

```javascript
helloWorld() // TypeError: helloWorld is not a function
var helloWorld = function() {
    console.log('Hello World!')
}
```

자바스크립트는 오직 선언부만을 호이스트하고, 초기화하지 않습니다. 그래서 helloWorld는 함수가 아닌 변수로 취급받습니다. 
* helloWorld는 var 변수이기에 엔진은 호이스팅 동안 undefined 값을 할당하게 됩니다.

위 코드를 에러 없이 제대로 호출하기 위해서는 아래와 같이 작성해야 합니다.
```javascript
var helloWorld = function() {
    console.log('Hello World')
}
helloWorld()
```

### var 변수 호이스팅
```javascript
console.log(a) // 'undefined' 출력
var a = 3;
```

자바스크립트는 초기화가 아닌 오직 선언부만을 호이스팅합니다. 즉 컴파일하는 동안, 자바스크립트는 할당값 대신 오직 함수와 변수 선언부만을 저장합니다. 

**[ undefined인 이유 ]**

자바스크립트 엔진이 컴파일 단계에서 var 변수 선언을 발견하면, 그 변수를 lexical 환경에 추가하고 코드에서 실제 할당이 이루어지는 라인에 도달한 뒤 undefined 변수에 그 값을 할당하여 초기화합니다.

**[ 위 상황의 초기 Lexical 환경 ]**
```javascript
lexicalEnvironment = {
    a: undefined
}
```

**[ 자바스크립트 엔진이 실제 할당을 끝낸 후 ]**
```javascript
lexicalEnvironment = {
    a: 3
}
```

### let과 const 변수 호이스팅
```javascript
console.log(a) // ReferenceError: a is not defined
let a = 3
```

모든 선언(function, var, let, const 및 class)은 자바스크립트에서 호이스팅되며, `var 선언`은 <u>**undefined로 초기화**</u>되지만 `let 및 const 선언`은 <u>**초기화되지 않은 상태로 유지**</u>됩니다.
* let과 const 및 class는 오직 lexical 바인딩(할당)이 자바스크립트 엔진 런타임 도중 평가될때에만 초기화가 됩니다. 즉, 자바스크립트 엔진이 소스코드에서 선언된 위치에 있는 변수를 평가하기 전까지 접근할 수 없다는 것입니다.
  * 이는 TDZ(Temporal Dead Zone)이라 불리며, **변수 생성과 접근불가한 곳이 초기화되기까지의 시간 간격**을 의미합니다.

만약 자바스크립트 엔진이 let, const 값이 선언된 라인에서 찾기 못하면, undefined 값을 할당하거나 error(const일 경우)를 반환합니다.
```javascript
let a
console.log(a) // outputs undefined
a = 5
```
* 컴파일 단계에서 자바스크립트 엔진은 변수 a와 마주쳐 lexical 환경에 저장하지만, let 변수이기 때문에 엔진은 어떤 값으로도 초기화하지 않습니다.

위 경우의 컴파일 단계에서의 lexical 환경은 아래와 같습니다.
```javascript
lexicalEnvironment = {
    a: <uninitialized>
}
```

* 만약 선언 전 변수에 접근하게 되면, 자바스크립트 엔진은 변수가 초기화되지 않았기 때문에 lexical 환경에서 변수의 값을 가져오려 하고, 이에 참조 에러가 발생합니다.

* 반면, 실행 중 엔진이 변수가 선언된 라인에 접근하면, 바인딩(값)을 평가하려고 시도할 것입니다. 이때 위와 같이 선언만 먼저 되고, 값이 나중에 바인딩되면 선언된 위치에서는 변수와 연관된 값을 찾지 못해 undefined를 할당합니다. 

### class 선언 호이스팅
let과 const 선언같이 자바스크립트의 class 또한 호이스팅되나, 컴파일 시점에는 초기화되지 않은 상태로 유지됩니다.

```javascript
let peter = new Person('Peter', 25)
// ReferenceError: Person is not defined

console.log(peter)

class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
}
```
이로 인해 class에 접근하기 위해서는 먼저 선언을 해야 합니다.

```javascript
class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }    
}
let peter = new Person('Peter', 25)
console.log(peter) // Person { name: 'Peter', age: 25 }
```

위 코드의 컴파일 단계에서 lexical 환경은 아래와 같습니다.
```javascript
lexicalEnvironment = {
    Person: <uninitialized>
}
```
자바스크립트 엔진에 의해 class가 초기화 되면 아래와 같이 lexical 환경이 바뀝니다.
```javascript
lexicalEnvironment = {
    Person: <Person object>
}
```

### class 표현식 호이스팅
함수 표현식처럼, class 표현식은 호이스팅되지 않습니다.
예를 들어, 아래와 같은 코드는 동작하지 않습니다.
```javascript
let peter = new Person('Peter', 25)
// ReferenceError: Person is not defined

console.log(peter)
let Person = class {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
}
```
위 코드를 올바르게 고치면 다음과 같습니다.
```javascript
let Person = class {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
}

let peter = new Person('Peter', 25)
console.log(peter) // Person { name: 'Peter', age: 25 }
```

### 호이스팅 착각하면 안되는 점
호이스팅은 자바스크립트가 현재 scope(함수 또는 전역)의 최상단으로 선언부(변수 및 함수)를 이동시키는 행위가 아니라는 점을 명심해야 합니다.
* 비록 호이스팅이 선언부를 코드 상단으로 올리는 것과 같이 느껴질 수 있으나, 실제로 코드가 움직이는 것은 아닙니다.

## 함수 표현식 VS 함수 선언식
### 함수 선언식(Function Declaration)
변수 선언이 `var`로 시작해야 하는 것처럼 함수 선언은 `function`으로 시작합니다. 선언된 함수는 추후 사용할 수 있도록 저장되며, 해당 함수를 호출할 때에 실행됩니다.

```javascript
function test() {
    return "Hello World!"
}

test(); // 이때 "Hello World!" 실행
```

### 함수 표현식(Function Expression)
함수 표현식이란, 함수가 변수로 저장해 <u>**변수를 함수처럼 사용 가능**</u>하게 하는 것입니다.

```javascript
var test = function (a, b) { return a + b }
```
* 위와 같이 변수에 저장된 함수는 함수명을 따로 지정할 필요 없고 <u>**변수 이름을 통해 호출**</u>합니다.

### 함수 선언식과 함수 표현식의 차이는 무엇일까?
```javascript
console.log(function_declaration())
console.log(function_expression()) // function_expression 함수가 아직 로드되지 않아 함수로 인지되지 않음

var function_expression = function() { return 5 }

function function_declaration() { return 5 }
```

위 코드를 실행하면 아래와 같은 에러가 발생합니다.

```bash
5
/Users/earth/Documents/JavaScript/test.js:2
console.log(function_expression())
            ^

TypeError: function_expression is not a function
```

함수 선언식은 코드가 실행되기 전에 로드되지만, 함수 표현식은 인터프리터가 해당 코드 줄에 도달할 때만 로드됩니다. 
* 함수 선언식은 var과 유사하게 호이스팅되지만, 함수 표현식은 호이스팅되지 않아 정의된 범위에서 로컬 변수의 복사본을 유지할 수 있습니다.

함수 선언식과 함수 표현식을 함께 사용할 수 있지만, 함수 표현식은 함수 이름이 필요 없어 가독성이 더 높다는 장점이 있습니다.

### 함수 표현식의 장점
함수 표현식을 사용할 때의 장점은 아래와 같으며, 하나씩 살펴보도록 하겠습니다.
1. 클로저
2. 인자 전달
3. IIFE

**[ 클로저 ]**
클로저란 <u>**함수가 종료되어도 lexical scope의 index와 같은 정보를 유지**</u>하는 것입니다.
```javascript
function navsHandler(index) {
    return function navClickEvent(evt) {
        // 이벤트 코드
    }
}

var navs = document.querySelectorAll('.nav')
var i

for (i = 0; i < navs.length; i += 1) {
    navs[i].onclick = navsHandler(i)
}
```
<u>**이벤트 핸들러는 반복이 완료된 후 실행**</u>되므로, **for 반복문의 올바른 값을 유지**하려면 <u>클로저가 필요</u>합니다.

```javascript
// 잘못된 예 1
var i

for (i = 0; i < list.length; i += 1) {
    document.querySelector('#item' + i).onclick = function doSomething(evt) {
        // i는 항상 list.length 값을 갖습니다.
    }
}

// 잘못된 예 2

var list = document.querySelectorAll('.item')
var i
var doSomething = function (evt) {
    // 이 함수가 실행될 때까지 i의 값은 루프에 있던 값이 아닙니다.
}

for (i = 0; i < list.length; i += 1) {
    item[i].onclick = doSomething
}
```
* for 반복문의 올바른 값을 유지하여 이벤트 핸들러를 실행하려면, index를 인자로 외부 함수에 전달하여 해당 값을 내부 함수에 전달해야 합니다.

일반적으로 내부 반환 함수에 필요한 정보를 구성하는 데 사용되는 핸들러 함수는 아래와 같습니다.
```javascript
var list = ['item1', 'item2', 'item3']
var i
var doSomethingHandler = function (itemIndex) {
    return function doSomething(evt) {
        // 클로저가 생성되어, itemIndex를 인자로 참조할 수 있게 됩니다.
        console.log(list[itemIndex])
    }
}

for (i = 0; i < list.length; i += 1) {
    item[i].onclick = doSomethingHandler(i)
}
```

**[ 인자 전달 ]**
함수 표현식은 <u>**중간 임시 변수에 할당할 필요없이 함수에 직접 전달**</u>이 가능합니다.
* 익명 함수의 형태로 jQuery에서 자주 볼 수 있습니다.
```javascript
$(document).ready(function () {
    console.log('익명 함수')
})
```

하지만, 아래처럼 `forEach()` 같은 메소드를 사용할 때에는 함수 표현식의 이름을 지정하는 것이 디버깅 시 편리할 수 있습니다.
```javascript
var productIds = ['bisu', 'boxer', 'nada']

productIds.forEach(function showProduct(productId) {
    ...
})
```

**[ IIFE(즉시 주입 함수 표현식) ]**
IIFE는 <u>**함수와 변수가 전역 스코프에 영향을 미치지 않도록 방지하는 데 사용**</u>됩니다. 
* IIFE 내의 <u>**모든 속성은 익명 함수로 범위가 지정**</u>됩니다. 
* 이는 코드가 다른 곳에서 부작용이 발생하지 않도록 방지하는 데 사용되는 일반적인 디자인패턴입니다.

또한, 아래와 같이 유지 관리하기 쉬운 섹션에 코드 블록을 포함하는 모듈 패턴으로도 사용됩니다.
```javascript
(function () {
    // 코드
}())
```

모듈로 사용하면 코드를 쉽게 유지 관리할 수 있습니다.
```javascript
var myModule = (function () {
    var privateMethod = function () {
        console.log('A private method')
    },
    someMethod = function () {
        console.log('A public method')
    },
    anotherMethod = function () {
        console.log('Another public method')
    }

    return {
        someMethod: someMethod,
        anotherMethod: anotherMethod
    }
}())
```

## 자바스크립트 관련 추가 내용

### 이벤트 핸들러
자바스크립트에서 이벤트 핸들러를 등록하는 방법은 세 가지가 있습니다.
1. HTML 요소의 속성으로 등록하는 방법
2. DOM 요소의 프로퍼티로 등록하는 방법
3. addEventListener 메소드를 사용하는 방법

**[ HTML 요소의 속성으로 등록하는 방법 ]**

HTML 요소로 버튼을 만들고 버튼의 속성 중 "onclick" 속성에 이벤트 처리 함수를 등록할 수 있습니다.
```html
<!DOCTPYE html>
<html>
<head>
    <meta charset='UTF-8'>
    <title>Javascript Example</title>
    <script>
        function displayTime() {
            var d = new Date()
            console.log("" + d.toLocalString())
        }
    </script>
</head>
<body>
    <input type="button" value="click" onclick="displayTime()">
</html>
```
* 주요 이벤트 처리 속성

|이벤트 처리 속성|설명|
|--------------|---|
|onclick|마우스로 클릭했을 때|
|ondbclick|마우스로 더블클릭했을 때|
|onmousemove|마우스 포인터가 HTML 요소 위에서 움직일 때|
|onmouseout|마우스 포인터가 HTML 요소를 벗어났을 때|
|onmouseover|마우스 포인터가 HTML 요소 위에 놓여있을 때|
|onkeypress|키보드의 키를 누르고 손을 떼었을 때|
|onchange|input 요소의 값이 바뀌었을 때|
|onfocus|input 요소에 포커스가 갔을 때|
|onblur|input 요서가 포커스를 잃었을 때|

**[ DOM 요소의 프로퍼티로 등록하는 방법 ]**

DOM(Document Object Model)은 자바 스크립트 등의 프로그램이 HTML 요소를 조작할 수 있도록 제공되는 인터페이스입니다. 
* document.write() 함수의 document가 DOM의 객체이고 window 객체 역시 DOM의 주요 객체입니다.

HTML 요소의 속성으로 등록하는 방법에서 사용한 스크립트를 DOM 요소의 프로퍼티를 통한 방식으로 변경해보도록 하겠습니다.
```html
<!DOCTPYE html>
<html>
<head>
    <meta charset='UTF-8'>
    <title>Javascript Example</title>
    <script>
        function displayTime() {
            var d = new Date()
            console.log("" + d.toLocalString())
        }
        window.onload = function() {
            var button = document.getElementById("button")
            button.onclick = displayTime
        }
    </script>
</head>
<body>
    <input type="button" value="click" id="button">
</html>
```
* window.onload 프로퍼티는 웹 브라우저가 HTML 문서를 다 읽었을 때 호출될 함수를 저장한 프로퍼티입니다.
* 여기에서 document 객체를 통해 "button"이라는 id를 가진 요소를 불러와 button 변수에 저장하고 onclick 프로퍼티에 이벤트 처리함수인 displayTime() 함수를 등록하여 사용했습니다.

**[ addEventListener 메소드 등록하는 방법 ]**

addEventListener() 메소드 사용법은 아래와 같습니다.
```javascript
target.addEventListener(type, listener(e), useCapture)
```
* target은 등록할 요소, 즉 document에서 읽어온 input 요소 등을 뜻합니다.
* type은 이벤트 타입(onclick. onmouseover 등)을 뜻합니다.
* listener는 등록할 이벤트 핸들러를 뜻합니다.
* useCapture는 이벤트 단계 중 캡쳐링 단계에서 실행할지 여부를 뜻하며 true, false 중 하나가 들어갑니다.

listener에 등록될 이벤트 핸들러에는 인수로 이벤트 객체를 받을 수 있으며, 이벤트 객체 안에는 발생한 이벤트에 대한 여러 정보가 담겨있습니다.

기존에 이벤트 핸들러 등록 예제로 사용한 스크립트를 `addEventListener()` 메소드 사용하는 것으로 변경해보도록 하겠습니다.
```html
<!DOCTPYE html>
<html>
<head>
    <meta charset='UTF-8'>
    <title>Javascript Example</title>
    <script>
        function displayTime() {
            var d = new Date()
            console.log("" + d.toLocalString())
        }
        window.onload = function() {
            var button = document.getElementById("button")
            button.addEventListener("click", displayTime, false)
            button.addEventListener("click", function(e) { console.log("second listener: " + e), false})
        }
    </script>
</head>
<body>
    <input type="button" value="click" id="button">
</html>
```
* DOM 요소의 프라퍼티로 등록하는 방법과 유사하지만, <u>**addEventListener 메소드를 이용할 경우 하나의 이벤트에 여러 핸들러를 등록**</u>할 수 있습니다.

### 자바스크립트, 세미콜론을 써야하나 말아야하나?
[자바스크립트, 세미콜론을 써야하나 말아야 하나](https://bakyeono.net/post/2018-01-19-javascript-use-semicolon-or-not.html)

위 글을 읽으면서, ASI가 이해할 수 있는 문장으로 쓴다면 굳이 세미콜론을 써지 않아도 되겠다는 생각이 들어 쓰지 않고 코드를 쓰는 습관을 들이고자 합니다.
* 세미콜론을 쓰면 안 되는 곳까지 세미콜론을 쓰는 오류를 범하느니 안 쓰는 게 나을 것 같습니다..


## 참고 자료
* [이벤트 핸들러](https://blog.naver.com/yuyyulee/221584032543)
* [함수 표현식 VS 함수 선언식](https://velog.io/@bisu8018/%ED%95%A8%EC%88%98-%ED%91%9C%ED%98%84%EC%8B%9D-VS-%ED%95%A8%EC%88%98-%EC%84%A0%EC%96%B8%EC%8B%9D)