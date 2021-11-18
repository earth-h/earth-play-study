### **들어가기 전에**

사내에서 HTTP에서 HTTPS를 호출하는 데, 쿠키가 제대로 동작하지 않는다는 문의를 받았습니다. 해당 이슈의 원인은 간단히 말해서, Same-Site가 Schemeful Same-Site로 변화되었음으로 인한 것이었습니다.

Chrome M88 업데이트부터 기존 Same-Site 정책이 Schemeful Same-Site으로 변화되었습니다. 이번 포스팅을 통해 Same-Site가 무엇인지와 이번 변화를 통해 바뀐 점이 어떤 것이 있는지 살펴보도록 하겠습니다.

### **Cookies?**

Cookie란 웹사이트의 상태를 유지하기 위한 방법 중 한 가지라고 생각하면 됩니다. Cookie는 수년에 걸쳐 발전해왔지만, 보안적인 이슈 등 해결해야할 부분이 아직 남아있습니다. 이러한 이슈 해결을 위해 Chrome, Firefox 및 Edge 등의 브라우저들은 개인 정보를 좀 더 안전하게 보호할 수 있도록 기본 동작을 바꿔나가고 있습니다.

Cookie는 `key=value` 형태를 가지고 있으며, **해당 Cookie가 사용되는 시기 및 위치를 제어하는 여러 속성과 함께 사용**됩니다. 예를 들어, HTTPS를 통해서만 전송되어야 하는 Cookie라면 Secure 속성을 갖게 됩니다.

서버에서는 `Set-Cookie` 헤더를 이용해 쿠키를 설정하며, 관련 예시는 아래와 같습니다.

> 신규 프로모션을 유저들에게 보여주고, 해당 프로모션을 닫은 유저는 한동안 해당 프로모션을 볼 수 없는 상황이라고 가정합니다.

이 경우 서버에 하기와 같이 Set-Cookie 설정을 진행할 수 있습니다.

```
Set-Cookie: promo_shown=1; Max-Age=2600000; Secure
```

-   한 달(2,600,000초) 후 만료되며, HTTPS를 통해서만 보낼 수 있는 Cookie

![서버는 Set-Cookie 헤더를 통해 Cookie를 설정합니다.](https://web-dev.imgix.net/image/tcFciHGuF3MxnTr1y5ue01OGLBn2/jJ1fqcsAk9Ig3hManFBO.png?auto=format&w=1428)

이때, 유저가 HTTPS를 통한 연결을 하고 있고, Cookie가 한 달 미만인 경우 브라우저는 Request에 아래와 같은 헤더를 추가하여 전송합니다.

```
Cookie: promo_shown=1
```

-   이렇게 전송하게 되면, 만료되지 않은 쿠키이기 때문에 프로모션을 해당 유저에 다시 보여주지 않습니다.

![브라우저는 Cookie 헤더에 쿠키를 다시 전송합니다.](https://web-dev.imgix.net/image/tcFciHGuF3MxnTr1y5ue01OGLBn2/Rq21WQpOZFvfgS9bbjmc.png?auto=format&w=1428)

Cookie 설정 시, 유의할 점은 Max-Age 속성을 이용해서 Cookie들이 필요 이상으로 오랜 시간동안 남아있지 않도록 해야 합니다.

-   호출이 잦은 페이지에 Cookie가 다량 설정될 경우 Request에 대한 오버헤드로 인한 first byte에 대한 딜레이가 발생할 수 있기 때문입니다.

#### **First-Party Cookie & Third-Party Cookie**

이전에 접속했던 사이트로 돌아가면, 현재 보이는 사이트에 대한 Cookie 뿐 아니라 다양한 도메인에 대한 Cookie가 있음을 확인할 수 있습니다. First-Party Cookie 및 Third-Party Cookie는 하기와 같은 개념이며 자신이 접속한 도메인이 어딘지에 따라 각 Cookie는 First-Party가 될 수도 있고 Third-Party가 될 수도 있습니다.

-   `First-Party Cookie`: 현재 사이트의 도메인과 일치하는 Cookie
-   `Third-Party Cookie`: 현재 사이트가 아닌 다른 도메인의 Cookie

![Cookie는 다양한 도메인으로부터 제공될 수 있습니다.](https://web-dev.imgix.net/image/tcFciHGuF3MxnTr1y5ue01OGLBn2/zjXpDz2jAdXMT83Nm3IT.png?auto=format&w=1428)

예를 들어, **A라는 사진(예: `testcdn.com/a.png` > `promo_shown=1` Cookie 세팅)**을 보고 마음에 들어 해당 사진 URL을 복사해서 자신의 블로그 포스팅에 붙여넣기를 한다고 가정합니다. 이 경우, 블로그 포스팅 내 A 사진에 대한 호출이 존재하여 A 사진에 대한 Cookie 역시 블로그 포스팅에 함께 들어가게 됩니다. 이 Cookie는 사실상 블로그 포스팅과는 관련이 없기 때문에 **Request에 대한 Overhead만 늘어나게** 됩니다.

물론, Third-Party Cookie가 유용한 경우(예: 블로그에 Youtube 동영상 삽입 시, 방문자가 추후 Youtube 방문 시 해당 영상이 추천으로 뜰 수 있음)도 있을 수 있지만, 이로 인한 보안 및 개인 정보 이슈가 발생할 수 있는 점을 무시할 수 없습니다.

예를 들어 CSRF(Cross-Site Request Forgery, 교차 사이트 요청 위조) 공격이 발생할 수 있으며, CSRF는 누가 Request를 시작했는지 상관없이 **Cookie가 주어진 origin에 대해 모두 첨부된다는 것에 의존된 공격**입니다.

이러한 상황을 해결하고자 나온 것이 **Same-Site 속성을 사용하여 Cookie 사용을 명시적으로 기술**하는 것입니다.

### **Same-Site 속성**

Same-Site는 **허용할 Cookie 범위를 지정하는 속성**입니다. Same-Site의 값으로는 하기 3가지가 설정될 수 있습니다.

![SameSite 속성 값](https://web-dev.imgix.net/image/tcFciHGuF3MxnTr1y5ue01OGLBn2/1MhNdg9exp0rKnHpwCWT.png?auto=format&w=1428)

-   `SameSite=Strict`: Same-Site에 대해서만 Cookie 허용
-   `SameSite=Lax`: Strict 속성에 일부 예외(GET 메소드를 사용하는 `<a href>` 또는 form의 GET 메소드(`<form method=get>`) 등)를 두어 Cross-Site에 대해 Cookie 허용 (현 Default 값 - Chrome 84부터)
-   `SameSite=None`: 도메인 상관없이 모든 Cookie 허용 - Same-Site 검증 X (기존 Default 값)
    -   **SameSite=None으로 설정하기 위해서는 Secure를 명시하여 Cookie를 사용해야** 합니다.

Same-Site의 **"Site"**란, **도메인 접미사와 바로 앞의 도메인 부분의 조합**입니다. 따라서, `www.earth.com`도메인은 `earth.com`의 일부입니다. 이 때, **public suffix**에 대해서는 **Same-Site가 아닐 수 있으니 유의**해야 합니다.

-   만약 필자가 `www.earth.com`에 접속해있고, `img.earth.com`을 통해 이미지를 호출해온다면, 이것은 Same-Site 요청입니다.
-   `github.io`의 경우 public suffix이기 때문에 `earth.github.io`에서 `earth-95.github.io`에 대한 호출을 한다면, 이것은 Cross-Site 요청입니다.

### **Schemeful Same-Site**

기존 Same-Site 개념의 경우, 동일한 도메인이라면 HTTP 사이트와 HTTPS 사이트를 Same-Site로 판단하였습니다. 이로 인해, SameSite 속성값과 상관 없이 동일 도메인 HTTP와 HTTPS간 Cookie 전송에 이슈가 없었습니다.

하지만, Schemeful Same-Site가 적용되어 URL scheme를 포함하도록 Same-Site 개념이 확장되었습니다. 따라서, 동일 도메인의 Cross-Scheme 요청은 Cross-Site 요청으로 인지됩니다.

-   Cross-Scheme란, 동일 도메인이지만 다른 Scheme를 가진 관계라고 볼 수 있습니다.
    -   예를 들어, [http://earth-95.tistory.com과](http://earth-95.tistory.com%EA%B3%BC) [https://earth-95.tistory.com은](https://earth-95.tistory.com%EC%9D%80) Cross-Scheme 관계입니다.

즉, **SameSite 속성을 Strict으로 설정**할 경우 **동일 도메인 HTTP와 HTTPS간 Cookie 전송은 불가능**하며, **상황에 따라 SameSite 속성이 Lax로 설정된 경우 Cookie 전송이 불가능**할 수 있습니다.

![기존 SameSite와 Schemeful SameSite 개념](https://blog.kakaocdn.net/dn/b0aEb2/btrlshPjPcS/zlQKjFGSkgQMXhMgu4m7j0/img.png)

Schemeful Same-Site 도입으로 인해, Cross-Scheme 상황이 발생할 수 있는 경우에 대해 알아보도록 하겠습니다.

#### **Cross-Scheme 시나리오(1) - Navigation**

예를 들어, **http**://earth-95.tistory.com에서 **https**://earth-95.tistory.com을 link하여 이동시킬 경우, 기존에는 `SameSite=Strict` 설정을 하여도 문제 없이 Cookie 전송이 가능했습니다. 하지만, Schemeful Same-Site 적용으로 인해 하기와 같이 `SameSite=Strict` 설정 시 Cookie가 전송되지 않습니다.

![Cross-Scheme navigation from HTTP to HTTPS](https://blog.kakaocdn.net/dn/cfdEow/btrlyY1AvG2/wKtMsvxfnDdyRKT3at4bX1/img.png)

#### **Cross-Scheme 시나리오(2) - Loading subresources**

-   subresources로는 iframe 또는 image 등을 생각할 수 있으며, XHR에 의한 네트워크 요청 및 Fetch 역시 포함됩니다.

기존에는 **Cross-Scheme의 서브 리소스 호출 시** Cookie를 보낼 수 있었습니다.

-   SameSite=Strict 또는 SameSite=Lax 설정에 대해 모두 허용

하지만, Schemeful Same-Site 적용으로 인해 `SameSite=Strict` 또는 `SameSite=Lax`에 대해 모두 Cookie를 허용하지 않게 되었습니다. 추가적으로, `SameSite=None`으로 설정할 경우 HTTP에서 HTTPS에 대한 리소스를 로드하는 것은 허용하나, **HTTPS에서 HTTP 리소스를 로드하여 Cookie를 설정하는 것은 허용하지 않습**니다.

![HTTP page including a Cross-Scheme subresource via HTTPS](https://blog.kakaocdn.net/dn/c6FnIQ/btrlvAVoWn8/nkjemWb4LvkzfcH1xs83r0/img.png)

#### **Cross-Scheme 시나리오(3) - Posting a form**

기존에는 Cross-Scheme 사이 form의 POST 메소드 요청을 통해 Cookie를 전송할 수 있었습니다.

-   `SameSite=Strict` 또는 `SameSite=Lax` 설정에 대해 모두 허용

하지만, 현재는 SameSite=None으로 설정되어 있을 경우에 한하여 Cross-Site POST에 Cookie 전송이 가능합니다. 추가적으로, `SameSite=None`으로 설정할 경우 HTTP에서 HTTPS로 form을 POST 메소드를 통해 전송하는 것은 허용하나, **HTTPS에서 HTTP로 form을 POST 메소드로 전송하며 Cookie를 설정하는 것은 허용하지 않습**니다.

-   즉, 가장 좋은 방법은 form page와 submit하여 도착할 경로 모두를 HTTPS로 지정하여 HTTPS로 통신하는 것이 좋습니다.

![Cross-Scheme form submission from HTTP to HTTPS](https://blog.kakaocdn.net/dn/crsQjU/btrlpMhJvh2/FKQ2sUePYcBJ3Cg08cZyd1/img.png)

### **마치며**

WEB 서비스라는 환경이 보안적으로 취약할 수 있는 부분(예: CSRF)이 많아, 그 부분을 해결해보고자 이러한 정책이 생겨난 것 같습니다. 처음부터 안전하게 서비스를 구성했더라면 이러한 변화가 생기더라도 어떻게 수정할 지 고민을 하지 않았을 것인데 이러한 부분을 놓친 점이 아쉽다는 생각이 듭니다. 앞으로는 좀 더 클린 코드 뿐 아니라 보안적인 측면에서 봤을 때 추후 이슈가 될 수 있어 보이는 포인트에 대해 생각하며 코드 구성을 해야할 것 같습니다.

### **참고 자료**

-   [Chrome Status - Schemeful same-site](https://chromestatus.com/feature/5096179480133632)
-   [Schemeful Same-Site](https://web.dev/schemeful-samesite/)
-   [Same-Site Cookie 개념](https://web.dev/i18n/en/samesite-cookies-explained/)
-   [Public Suffix 리스트](https://publicsuffix.org/list/public_suffix_list.dat)