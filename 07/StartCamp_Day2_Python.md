## CLI&GUI

| 차이점        | CLI    | GUI    |
| ------------- | ------ | ------ |
| 상호작용 방식 | 터미널 | 그래픽 |
| 사용 도구     | 텍스트 | 마우스 |
|               |        |        |

**Git** ; 분산 버전 관리 시스템

**버전관리** ; 변화를 기록하고 추적하는 것

## CLI 명령어

### cd

- `cd` Change Directory ; Directory 변경

  - `cd .` 현재 Directory 이동 ;아무일 없음
  - `cd ..` 상위(부모) Directory로 이동
  - `cd /` Root Directory로 이동
  - `cd ~` 터미널의 기본 시작 Directory로 이동
  - `cd <folderName>` 해당 폴더로 이동

### ls

- `ls` 해당 Directory의 폴더/파일 리스트 보기

  - `ls -a` 해당 Directory의 숨겨진 폴더/파일까지 리스트 보기
  - `ls <Path>` 해당 Path의 폴더/파일 리스트 보기 ex) `ls ~/Desktop` ; Desktop의 파일/폴더 리스트 보기

### touch

- `touch <fileName>` `fileName`을 이름으로 하는 파일 생성 ; 확장자까지 작성 必

### mkdir

- `mkdir <folderName>` `folderName`을 이름으로 하는 폴더 생성

### rm

- `rm <fileName>` `fileName` 파일 삭제

  - `rm -r <folderName>` `folderName` 폴더 삭제 (`rmdir <folderName>`과 동일 기능)
  - `rm -f <name>` `name` 강제 삭제

<br>

## 중앙 VS 분산

- 중앙집중식 : 버전은 중앙서버에 저장되고 중앙서버에서 파이을 가져와 다시 중앙에 업로드
- 분산식 : 버전을 여러 개의 복제된 저장소에 저장 및 관리

<br>

#### 분산구조의 장점

- 중앙 서버에 의존하지 않고 동시에 다양한 작업을 수행할 수 있음
- 중앙 서버의 장애나 손실에 대비하여 백업과 복구가 용이
- 인터넷에 연결되지 않은 환경에서도 작업을 계속할 수 있음
  - 변경 이력을 개인 저장소에 저장하고 나중에 중앙 서버와 동기화

#### Working Directory

- 실제 작업중인 파일들이 저장되는 영역

#### Staging Area

- Working Directory에서 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

#### Repository

- 버전 이력(COMMIT)과 파일들이 영구적으로 저장되는 영역
- 모든 버전과 변경 이력이 기록됨

<br>

## Git

### git init

- `git init` ; 로컬 저장소 설정(초기화)

  - git의 버전 관리를 시작할 디렉터리에서 진행
  - 주의사항 : **Git 로컬 저장소 내부에 또 다른 Git을 추가하지 말 것**
    - 내부의 변경사항 추적 불가

### git config

- Author 설정하기
- ```
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
  ```
  - `--global` 옵션은 Repository 별로 다르게 하고 싶으면 빼고 설정
  - `git config --global -l` ; 현재 설정 보기

### git add

- `git add <name>, ...` ; 변경사항이 있는 파일/폴더를 Staging Area에 추가
  - `git add .` 현재 Directory의 모든 변경내용 추가
  - `git add a.txt` ; a.txt파일 추가
  - `git add a.txt, /dir` ; a.txt파일과 dir폴더 추가
  - `git add *.txt` ; 확장자가 .txt인 파일 모두 추가

### git commit

- `git commit` ; Staging Area에 있는 파일들을 저장소에 기록

  - 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
  - `git commit -m '<COMMIT_Name>'` ; `COMMIT_Name`의 커밋 생성
  - `git commit --amend` ; Vim Editor를 사용하여 직전 커밋 메세지 수정 가능 (빠진 파일 추가 or 메세지 명 변경)

    - 파일 추가 시 빠진 파일을 먼저 add 한 뒤 commit

    참고 ; [Vim Editor 사용법](https://terms.naver.com/entry.naver?docId=4125944&cid=59321&categoryId=59321&expCategoryId=59321)

### git status

- `git status` ; 현재 Working Directory에 있는 파일의 상태를 보여줌

### git rm

- `git rm --cashed <name>` ; Staging Area에서 COMMIT 대기 중인 `name` 삭제

### git log

- `git log` ; Git에 COMMIT한 기록 보기
  - `git log --oneline` COMMIT기록 짧게 축약하여 보기
  - `HEAD`는 최신의 COMMIT에 붙음
