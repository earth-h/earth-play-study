## Ansible

Ansible은 shell과 같은 기존의 비정형 스크립트를 자동화 관점에서 기능을 모듈화하여 쉽게 기능을 구현할 수 있도록 지원하는 언어로, Python + YAML(YAML Ain't Markup Language) 포맷 기반으로 만들어진 자동화 언어입니다.

내부 구조가 Python이기는 하지만, Ansible 모듈을 직접 개발하지 않는 이상 Python 코딩을 할 필요는 없습니다. 

### 장점 1 - 쉽다

Ansible은 스크립트 수준에서 작성이 가능합니다. 물론 모듈의 종류나 기본적인 조건문, 권한 처리 등 기존에 없던 편의 기능을 사용하기 위한 기본적인 학습 비용은 발생합니다. 참고로, YAML의 들여쓰기 고통을 피하기 위해서는 IntelliJ, Eclipse 등의 IDE(Integrated Development Environment)에 Ansible 관련 플러그인을 추가해 사용하는 것이 좋습니다.

### 장점 2 - 직관적이다

이미 모듈화되어 있는 대부분의 기능을 사용하려고 할 때, 입력 항목이 정의되어 있고 예제가 제공되므로 큰 어려움 없이 사용할 수 있습니다. Ansible galaxy 사이트([https://galaxy.ansible.com/](https://galaxy.ansible.com/))에는 우리가 일반적으로 상상할 수 있는 대부분의 시스템 작업에 대한 샘플이 존재합니다.

### Ansible 사용 방법

처음 Ansible을 실행하기 위해 이해해야 하는 부분은 Ansible Ad-Hoc과 Playbook입니다. 단일 작업(task)을 수행하는 것을 Ad-Hoc Command라고 부르며 아래와 같이 수행합니다.

- 아래는 기본 옵션까지 모두 표현되어 있어 길어보이지만, 실제 사용시에는 생략 가능합니다. 다만, Ad-Hoc으로 여러 작업을 수행하려면 여러 번 실행해야 합니다.

```yaml
#대상 서버의 서비스를 제어(재구동)하는 Ad-Hoc
Ansible testservers --check --inventory=hosts --user=normaluser --become --become-user="root" --become-method="sudo" --ask-become-pass --module-name=service --args="name=firewalld state=restarted"
#설명
 --check : test로 수행합니다. 실제 작업이 수행되지 않습니다
 --inventory=hosts : 작업 대상 서버의 목록이 들어 있는 파일의 위치입니다
 --user=normaluser --become --become-user="root" --become-method="sudo" --ask-become-pass  : 대상 서버에 normaluser 계정으로 SSH 접속을 합니다. become으로 root 권한을 획득하고, pasword를 물어봅니다.
 --args="name=firewalld state=restarted" : 방화벽 서비스(firewall)를 재구동합니다.
```

여러 작업을 조합해서 실행해야 한다면 작업을 모아서 작성할 수도 있습니다. 이를 'playbook'이라고 부릅니다. 앞서 Ad-Hoc을 이용해서는, 서비스만 재구동했다면, playbook을 이용하면 방화벽 정책을 반영한 후 재구동할 수 있습니다.

```yaml
# 작업 대상 서버를 지정하고, sudo를 사용하여 root로 권한을 승격합니다.
- hosts: target_list
  become: yes
  become_user: root
  become_method: sudo
#dns와 ntp 포트의 접속을 허용합니다.
  firewalld:
    service: {{ item }}
    permanent: yes
    state: enabled
  with_lines:
      - dns
      - ntp
#방화벽 서비스를 재구동합니다.
- name: Restart the firewalld daemon
  service:
    name: firewalld.service
    state: restarted
```

위 예시에서 'Role'에 대한 부분은 없으나, 하나의 작업을 위해 필요한 여러 작업(task)을 모아 놓은 playbook을 Role이라는 재사용 가능한 형태로 만든다고 이해할 수 있습니다.

Playbook의 구조를 표현하면 아래와 같습니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ddd48657-7109-40a4-8583-d7f2767b7cb1/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ddd48657-7109-40a4-8583-d7f2767b7cb1/Untitled.png)

즉, Task로 이루어진 단일 yml 파일 또는 Role 구조(J2EE의 WAR와 같은 Ansible의 명세(specification))를 조합해서 만든 것을 playbook이라고 부릅니다. 

playbook 실행 명령어는 아래와 같습니다.

```yaml
# Restart_Firewalld_Service.yml  Playbook을 실행합니다.
Ansible-playbook --check --inventory=hosts Restart_Firewalld_Service.yml

#설명
 --check : test로 수행합니다. 실제 작업이 수행되지 않습니다
 --inventory=hosts : 작업 대상 서버의 목록이 들어 있는 파일의 위치입니다
Restart_Firewalld_Service.yml : 해당 playbook 파일을 실행합니다

!! 실행 user가 대상 서버들에 접속할 수 있도록 SSH pub key가 배포되어 있어야 하고, 실행하는 서버에 private key를 가지고 있어야 합니다. 옵션으로 SSH Key위치를 지정하거나 패스워드를 입력받을 수 있습니다.
!! 권한 변경을 위한 become이나 실행할 Inventory group 정보는 Playbook 내부에 정의되므로 별도로 옵션을 줄 필요는 없습니다
```

Ansible은 모듈을 조합하고, 조건을 관리하는 언어일 뿐 작은 단위의 실행에서는 CLI(Command-line Interface) 형태(Ad-hoc)로 작업할 수 있지만, 기업에서 사용자 권한 설정, SCM(Source Control Management) 도구 접속 관리, 병령/분산 처리, 실행 결과 로그 등등의 필수적인 기능은 제공하지 않으므로 직접 구현해야 합니다. 기업에서 사용하기 위한 기능에서 일부는 안되고, 일부는 따로 구현이 필요하여 해당 부분을 지원하는 솔루션으로 Ansible Tower라는 제품을 Redhat에서 제공(판매)합니다.

### AWX란?

2015년 Ansible을 이끌던 Ansible, Inc를 Red Hat에서 인수했습니다. Red Hat은 AnsibleWorks, Inc. 시절부터 개발된 Asible Worker를 OSS(Open Source Software)로 공개하기로 하였고, 기존 소스의 패키지 이름인 aws를 사용해 AWS Project가 시작되었습니다.

⇒ Ansible Tower의 OSS(Open Source Software) 버전이 AWX입니다.

AWX 자체는 Ansible 언어를 운영하는 미들웨어의 성격을 띄고 있습니다. Playbook이 없다면 할 수 있는 일은 거의 없어 사실상 Ansible playbook을 만드는 것이 중요합니다. AWX는 playbook을 관리하고 운영하는데 필요한 여러 기능을 제공합니다.

JAVA를 예로 들면 CLI(Command Line Interface) 환경에서 바로 실행되도록 개발(독립 데몬(daemon) 형태)할 수 있지만, 웹 서비스를 위해 WAR(Web Applicatio nArchive) 형태로 개발하여 Tomcat 등의 미들웨어 환경에서 운영할 수도 있습니다. 

Ansible 역시 CLI에서 직접 수행할 수도 있지만, 여러 부가 기능과 권한 관리 등을 지원하기 위해 AWX에 Ansible 코드(playbook)를 등록하여 수행합니다.

### 기업에서 AWX를 사용해도 되나요?

AWX는 Apache 2.0 라이선스를 따릅니다. Apache 2.0에서는 소스 수정 시 코드 공개를 강제하지 않습니다. 따라서, 기업에서 사용할 수 있고, 오히려 AWX를 이용해 외부에 소스를 공개하거나 상용 솔루션 등을 만들 경우에 대해서 여러 조건 사항이 있으므로 그런 경우에 확인이 필요합니다.

AWX 프로젝트는 공개되어 있으며, Git([https://github.com/ansible/awx](https://github.com/ansible/awx))에서 다운로드하여 설치한 뒤 사용할 수 있습니다. 다만, 기업에서 사용하려면 일부 설치 코드를 직접 조정해야 할 수 있습니다. 이러한 부분은 고가용성(High Availability) 등을 요구하는 환경에서 필요하며, 단순히 단일 노드로 운영하기 위한 설치는 어렵지 않습니다.

### 출처

[프로비저닝 자동화를 위한 Ansible AWX, 설치부터 엔터프라이즈 환경 적용까지 - 1 - LINE ENGINEERING](https://engineering.linecorp.com/ko/blog/ansible-awx-for-provisioning-1/)