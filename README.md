## 개요
우리 팀 ‘Sharks’ 팀원들의 공통 관심사인 모의 해킹을 목표로 시작된 프로젝트다.  
모의 해킹에 앞서 선행 학습으로 Front-End와 Back-End 모두 구축해보고,
‘상어’처럼 날카로운 취약점을 찾아 다양한 해킹 기법을 시도해 보고자 한다.
<br><br>
## 사용 기술
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat&logo=next.js&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
<br><br>
## 설치 및 실행 방법(wsl에서 진행)
* pyenv, pyenv-virtualenv 설치
  ```
  curl https://pyenv.run | bash
  ```
* pyenv 설정
  ```
  sed -Ei -e '/^([^#]|$)/ {a \
  export PYENV_ROOT="$HOME/.pyenv"
  a \
  export PATH="$PYENV_ROOT/bin:$PATH"
  a \
  ' -e ':a' -e '$!{n;ba};}' ~/.profile'$!{n;ba};}' ~/.profile
  ```
  ```
  echo 'eval "$(pyenv init --path)"' >>~/.profile
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
  ```
* pyenv로 python 설치
  ```
  pyenv install 3.7.13
  pyenv install 3.8.13
  ```
* python 가상 환경 설치
  ```
  pyenv virtualenv 3.7.13 django-envs
  ```
* python 가상 환경 적용
  * 전역에 적용
    ```
    pyenv global 3.8.13
    ```
  * 특정 디렉토리에 적용
    ```
    pyenv local django-envs
    ```
* 장고 설치
  ```
  pip3 install django==2.2
  ```
* 장고 개발 서버 실행
  ```
  python manage.py runserver
  ```
  <br>
## UI 및 기능
* 메인 페이지
  ![image](https://github.com/lux-02/sharks/assets/102010541/403a2872-ef59-4cac-9cdc-f74bbbaa14f0)<br>
* 블로그 페이지
  ![2023-10-30 02;18;47](https://github.com/lux-02/sharks/assets/102010541/8402f42b-3c20-458e-a407-a65131cfa9aa)<br>
* 글 작성 페이지
  ![image](https://github.com/lux-02/sharks/assets/102010541/86fc0fab-b65d-4dc7-9e58-3a294ecacacc)<br>
 
* 회원가입
  * 아이디와 이메일 중복 여부 확인
  * 패스워드 일치 여부 확인
  * 패스워드 복잡도 검사

   ![image](https://github.com/lux-02/sharks/assets/102010541/2341cbe9-5e87-43f0-a1a7-cbe0bab2e2a4)<br>


* 로그인
  * 유저 존재 여부 확인
    
  ![image](https://github.com/lux-02/sharks/assets/102010541/e6e8e65e-7c69-421c-832c-a8fd21b51f33)<br><br>




## DB ERD
![image](https://github.com/lux-02/sharks/assets/102010541/629a7d31-9d7f-4e33-b31f-9a8e0ba4fca6)





