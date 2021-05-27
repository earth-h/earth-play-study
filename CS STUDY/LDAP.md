# **LDAP 이란?**

## Lightweight Directory Access Protocol

- 네트워크 상에서 조직이나 개인정보 혹은 파일이나 디바이스 정보 등을 찾아보는 것을 가능하게 만든 소프트웨어 프로토콜
- 네트워크 상의 디렉토리 서비스 표준인 X.500의 DAP(Directory Access Protocol)를 기반으로 한 경량화(Lightweight) DAP 버전
    - DAP는 OSI 전체 프로토콜 스택을 지원하며 운영에 매우 많은 컴퓨팅 자원을 필요로 하는 무거운 프로토콜
    - LDAP은 DAP의 복잡성을 줄이고 TCP/IP 레이어에서 더 적은 비용으로 DAP의 많은 기능적인 부분을 조작할 수 있도록 설계
- 디렉터리 서비스?
    - 이름을 기준으로 대상을 찾아 조회하거나 편집할 수 있는 서비스
    - DNS도 디렉터리 서비스의 일종
        - DNS는 도메인 이름으로 IP 주소 조회
- LDAP 클라이언트?
    - 회사에서 관리하는 임직원 데이터베이스 등은 LDAP 서버로 운영되므로, 해당 부분을 서버라고 볼 수 있음
    - 클라이언트는, 각종 주소록 어플리케이션이라고 볼 수 있음
- Lightweight 하다.
    - 이 의미는 사용하기 간편하다가 아닌, 통신 네트워크 대역폭 상의 가벼움을 의미
    - 인터넷 프로토콜로, 데이터를 조금만 주고 받아도 되도록 설계
    - LDAP 요청의 99%는 검색에 대한 요청
    - 디렉토리 안에는 연락처, 사용자, 파일, code 등 무엇이든 넣을 수 있고, insert/update보다는 검색 요청에 특화되어 있음
    - 검색에 특화되어 있다보니, 트랜잭션이나 롤백이 없고 복잡한 관계도 설정할 수 없음
    - 신뢰성이나 가용성을 개선하기 위해 쉽게 복제될 수 있는 아키텍처로 이루어짐
- 기본적으로 바이너리 프로토콜
    - ASN.1이라는 언어로 메시지 표현
    - 메시지를 BER(Basic Encoding Rules)라는 포맷으로 인코딩하여 주고 받음
        - BER 인코딩은 **바이너리라서 내용을 알아볼 수 없음**
- 비동기 프로토콜
    - **세션을 하나만 열어 여러 메시지 요청을 보낼** 수 있고, **각각의 요청에 대한 응답이 다른 시점**에 올 수 있음
        - HTTP/1.1 프로토콜의 경우 클라이언트가 요청 보내면 해당 요청에 대한 답을 받고자 기다립니다(일종의 동기식 메시지 프로토콜).
    - 응답마다 어떤 요청의 응답인지 식별할 수 있는 아이디가 부여됨
    - 요청 메시지들의 순서와 그에 대한 응답 메시지들의 순서는 상이할 수 있음

## **용도**

- 사용자, 시스템, 네트워크, 서비스, 어플리케이션 등의 정보를 트리 구조로 저장하여 조회하거나 관리
- 회사에서 구성원의 조직도나 팀별 이메일 주소 등도 LDAP 서비스로 관리
    - 특정 영역에서 이용자명과 패스워드를 확인하여 인증하는 용도로 쓰임
- 인증을 포함하여 트리 구조로 검색하고 편집하기 좋은 데이터들은 LDAP을 많이 사용
- LDAP은 서버에만 적용되는 프로토콜이 아닌, 주소록 관리에 사용되거나 스마트폰 내에서도 LDAP 클라이언트가 포함되어 있음
- 특정 데이터를 중앙에서 일괄 관리하는 일반적인 경우에 사용
    - 유저 권한 관리, 주소록, 조직도, 사용자 정보 관리, 어플리케이션/시스템 설정 정보, 공개 키 인프라스트럭쳐, DHCP나 DNS등의 저장소, 문서 관리, 이미지 저장소, Code 등

## **주요 용어**

- **DN**: Distinguish Name
- **RDN**: Relative Distinguished Name
- **DIT**: Directory Information Tree
- **LDIF**: LDAP Data Interchange Format
- **UID**: User ID
- **DC**: Domain Component
- **OU**: Organizational Unit

## **LDAP 인증 FLOW**

![LDAP 인증 FLOW](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlFwkV%2FbtqHT1ce8qb%2Fk6KfyzcwwF68hraSlFiWEK%2Fimg.png)

## **LDAP 디렉토리 구조**

![LDAP 디렉토리 구조](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbub5ZE%2FbtqH0qB7Iwi%2Fm9aVKNNXYNnEt3sp6UxY0k%2Fimg.png)

LDAP 서버에는 여러 디렉토리 정보(entry)가 계층적 트리 구조(hierarchical tree-like)로 구성되어 있다.

- Entry 정보 참조는 RDN(Relative Distinguished Name)이나 DN(Distinguished Name)을 사용해서 정보를 얻을 수 있다.
- 각각의 엔트리는 다수의 속성을 갖는다.
- 각 속성은 (이름, 값 +) 형태
    - 이름 하나에 한 개 이상의 값이 바인딩 될 수 있음
- **각 엔트리는 DN(Distinguished Name)이라는 고유한 값으로 지칭**
    - 이 값으로 어디에 속한 엔트리인지 파악 가능
    - 예를 들어, 디렉토리의 파일이라고 치면 /home/earth/ldap.md 와 같은 전체 경로가 **DN**이라고 볼 수 있고, /home/earth가 **상위 엔트리의 DN**입니다.

## **도구**

- LDAP 서버를 구축에는 여러 옵션이 존재한다.
    - Widnwos 라이센스가 있다면 Active Directory가 적합
    - 오픈 소스: OpenLDAP, Apache DS, OpenDJ, 389 Directory Server 등
    - MAC의 디렉토리 유틸리티
        - 임의의 LDAP 서버에 붙어 내용을 간편하게 확인 가능
    - Apache Directory Studio
        - 이클립스 UI라 이클립스에 익숙하다면 편리함

## AD(Active Directory)

- AWS
    - Simple AD: 관리형 디렉토리 서비스
        - 사용자 계정, 그룹 멤버십, Amazon EC2 인스턴스들에 대한 도메인 조인
    - Microsoft AD; Windows Server 2012 R2 기반으로 운영되는 관리형 AD 서비스
        - SSO 지원
    - AD Connector
        - 온프레미스 AD 환경을 AWS 환경에서 사용할 수 있도록 해주는 Proxy 역할
- Trust
    - 단방향(One-way): 보안이 중요한 온프레미스에서 AWS 환경으로만 접근을 허용하려는 경우 단방향 Trust 구성
    - 양방향: 양쪽 모두에서 데이터 접근해야 하는 경우 양방향 Trust 구성

## **LDAP이 지원하는 명령어들**

대부분의 네트워크 서비스와 마찬가지로, LDAP 클라이언트가 LDAP 서버에 커넥션을 열어 각종 요청 메시지를 보낼 때 해당 요청 메시지에 들어갈 명령어들은 아래와 같습니다.

- StartTLS: 보안 암호화를 위해 현재 세션을 TLS로 업그레이드하는 확장 명령어
    - 현재 표준은 세션 열어 열자마자 StartTLS로 업그레이드하는 것(SMTP 프로토콜도 비슷함)
- Bind: 인증하고 LDAP 프로토콜 버전을 명시
- Search & Compare: 디렉토리 엔트리를 검색해서 조회합니다. 특정 엔트리에 어떤 속성 값이 있는지 확인 할 수 있음
- Add: 새 엔트리를 추가함
- Delete: 특정 엔트리를 삭제
- Modify: 특정 엔트리의 속성 값을 추가/제거/변경
- ModifyDN: 특정 엔트리의 디렉토리 위치를 바꾸거나 이름 바꿈
- Abandon: 직전에 보낸 요청을 취소해달라는 요청으로, 서버가 무시해도 무방
- Unbind: 더 이상 할 일이 없어 커넥션을 끊기 전에 보내는 명령어로, 서버가 해당 명령을 받으면 해당 클라이언트를 위해 확했던 리소스를 다 해제함