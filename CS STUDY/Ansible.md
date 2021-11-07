# ANSIBLE

## 목차
* [Ansible 개요](#ansible-개요)
* [Ansible Inventory](#ansible-inventory)
* [Ansible Role](#ansible-role)
  * [Role Directory Structure](#role-directory-structure)
* [Ansible에서 변수에 대한 값을 받아오는 우선순위](#ansible에서-변수에-대한-값을-받아오는-우선순위)
* [참고 자료](#참고-자료)

## Ansible 개요

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

## Ansible Inventory
Ansible을 사용하기 앞서 Ansible로 관리하려는 노드(서버)들의 정보가 들어있는 파일이 필요합니다. 이를 Inventory 파일이라고 하여 hostfile이라고도 불립니다. Ansible을 실행할 때 Inventory를 지정하지 않으면 `/etc/ansible/hosts` 파일을 불러오게 되며, `-i` 옵션을 통해 직접 inventory 경로를 지정할 수 있습니다.
* Inventory 파일 양식은 INI 또는 yaml 형식입니다.
  * 현재 사내에서 사용하는 Inventory 파일 형식은 INI를 띄고 있어 아래와 같은 형태입니다.
    ```yaml
    [web1]
    webserver11 ansible_host=10.10.10.10  # 10.10.10.10 IP에 대한 별칭은 webserver11이라고 지정한 것이며, 사내에서는 hostname을 그대로 넣고 있음
    webserver12 ansible_host=10.10.10.11    
    [web2]
    webserver21 ansible_host=10.10.10.12
    webserver22 ansible_host=10.10.10.13

    [web:children]
    web1
    web2

    [all:vars]
    ansible_user=username
    ansible_ssh_pass=password
    ansible_become_pass=rootPassword
    ```

## Ansible Role
**[Role 생성 명령어]**
```bash
ansible-galaxy init <ROLE_NAME>
```
### Role Directory Structure
```yaml
roles-example/ # role 이름
├── defaults # variables에 대한 default값 설정
│   └── main.yml
├── files # role에서 사용할 files들 보관
├── handlers # ansible handlers 보관
│   └── main.yml
├── meta # galaxy.ansible.com에 role을 release할 때 사용됨(authorship info)
│   └── main.yml
├── README.md
├── tasks # role은 tasks의 main.yml을 시작점으로 하여 구동됨
│   └── main.yml
├── templates # role에서 사용할 templates 보관(Jinja2 언어 사용)
├── tests # role에 대한 test 진행 시 사용
│   ├── inventory
│   └── test.yml 
└── vars # 현 role에서 사용할 변수를 선언하며, 다른 role에서는 사용할 수 없음
    └── main.yml
```
* defaults
  * variables에 대한 default값 설정
  * 변수 값 설정 시 가장 우선순위가 낮게 되어 있어 이 곳 외에 변수에 대한 값이 설정되어 있지 않을 경우만 사용됨
* files
  * role을 사용하면서 필요한 파일들을 넣어두고 사용
  * role의 task에서 files에 넣어둔 파일의 경로를 표시할 때 절대경로가 필요하지 않고 files를 시작점으로 했을 때의 파일 경로를 넣으면 됨
    * 예) files/web/prod-web.xml의 경우 task에서 web/prod-web.xml으로 표현
* handlers
  * Ansible handlers 보관소
  * ansible-playbook 실행이 완료된 후 상황에 맞게 handler 작동(이벤트 발생 시 구동된다고 보면 됨)
* meta
  * galaxy.ansible.com에 role을 출판하려 할 때 사용되는 info
  * 저자가 누구인지 등 role에 대한 라이센스 표시
* tasks
  * role은 tasks의 main.yml을 시작점으로 하여 구동됨
  * 사내에서 사용 시, main.yml을 통해 다른 yml 파일을 상황에 맞게 include하는 식으로 사용
* templates
  * files과 비슷하게 role에서 사용할 파일들을 저장
  * files와 다른 점은 파일 내용을 수정할 수 있다는 점이며, Jinja2 문법을 사용해서 templates 내 파일에 작성하면 상황에 맞게 파일 내용을 수정하여 배포 가능
  * .j2 확장자를 가진 파일들을 보관한다고 볼 수 있음
* tests
  * role에 대한 tests 스크립트 작성
  * tests 디렉토리에는 tests할 때 사용할 inventory가 따로 존재함
* vars
  * 생성한 role에 필요한 변수들을 선언하는 파일이며, 해당 role에서만 사용이 가능함
  * 다른 role과 충돌이 날 수 있는 변수들이 있다면 vars에 넣어 사용하는 것이 좋음

## Ansible에서 변수에 대한 값을 받아오는 우선순위
**가장 위에 있는 것이 우선순위가 제일 높음**
1. extra vars (for example, -e "user=my_user")(always win precedence)
2. include params
3. role (and include_role) params
4. set_facts / registered vars
5. include_vars
6. task vars (only for the task)
7. block vars (only for tasks in block)
8. role vars (defined in role/vars/main.yml)
9. play vars_files
10. play vars_prompt
11. play vars
12. host facts / cached set_facts 
13. playbook host_vars/* 
14. inventory host_vars/* 
15. inventory file or script host vars 
16. playbook group_vars/* 
17. inventory group_vars/* 
18. playbook group_vars/all 
19. inventory group_vars/all 
20. inventory file or script group vars 
21. role defaults (defined in role/defaults/main.yml) 
22. command line values (for example, -u my_user, these are not variables)

## 참고 자료
* [프로비저닝 자동화를 위한 Ansible AWX, 설치부터 엔터프라이즈 환경 적용까지 - 1 - LINE ENGINEERING](https://engineering.linecorp.com/ko/blog/ansible-awx-for-provisioning-1/)
* [Ansible 변수 주입 우선순위](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html)
* [Ansible directory 구조](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html)
* [Ansible Role directory 구조](https://blog.knoldus.com/ansible-roles-directory-structure/)