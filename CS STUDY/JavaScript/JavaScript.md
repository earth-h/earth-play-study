## 호이스팅


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