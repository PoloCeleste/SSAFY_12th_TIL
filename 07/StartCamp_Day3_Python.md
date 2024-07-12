# Remote Repository

### 원격 저장소

코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간

[github 사용법](https://training.github.com/downloads/ko/github-git-cheat-sheet/)

### git remote

- `git remote add <Nickname> <remote_repo_url>` ; 로컬 저장소에 원격 저장소 연결
  - `Nickname` ; 원격 저장소 별칭.
  - `git remote -v` ; 연결된 Repo 확인
  - `git remote remove <Nickname>` ; `Nickname` 을 별칭으로 하는 원격 저장소 연결 제거

### git pull

원격 저장소의 내용이 로컬에도 존재하는 경우 사용

- `git pull <Nickname> <branch_Name>` ; COMMIT 내용을 `branch_Name`으로 `Nickname`에 `pull`하기
  - `fatal: refusing to merge unrelated histories` 메세지 뜨는 경우<br> -> `git pull <Nickname> <branch_Name> --allow-unrelated-histories` 명령어로 프로젝트 병합.<br>-> git에서는 서로 관련 기록이 없는 이질적인 두 프로젝트를 병합할 때 기본적으로 거부하며, 이것을 허용해주는 옵션

### git push

- `git push <Nickname> <branch_Name>` ; 연결된 원격 저장소에서 로컬 저장소로 가져오기

  - `error:failed to push some refs to` 에러 발생 시 pull 작업 후 다시 push
    <br>-> 원격 저장소에 로컬에 없는 파일이 있을 때 push 할 경우 발생
  - COMMIT 이력이 없으면 push 불가

- 협력자를 추가해야 팀과 함께 작업 가능.<br>Github 해당 Repo의 Setting에서 팀원 초청.<br>Collaborators 메뉴에서 팀원 검색하여 추가.

### git clone

원격 저장소의 내용이 로컬에 존재하지 않는 경우 사용

- `git clone <remote_repo_url>` ; 원격 저장소 전체를 복제
  <br>-> Git으로 관리되고 있는 폴더 내부에서는 불가

<br><br>

## gitignore

Git에서 특정 파일이나 Directory를 추적하지 않도록 사용하는 텍스트 파일
<br>이미 git에 올라가있는 파일이나 Directory의 경우에는 추후에 gitignore에 추가하여도 등록되지 않음

[gitignore 생성 사이트 (gitignore.io)](https://www.toptal.com/developers/gitignore/)

- gitignore 예시
  1. .gitignore 파일 생성 (파일명 앞에 '.' 입력, 확장자 없음)
  2. a.txt와 b.txt 파일 생성
  3. gitignore에 a.txt 작성
  4. `git init`
  5. `git status`

<br><br>

# Git revert & reset

## revert

- 재설정
- 단일 COMMIT을 실행 취소 하는 것
- 프로젝트 기록에서 COMMIT을 없었던 일로 처리 후 그 결과를 새로운 COMMIT으로 추가함
- 기록에서 COMMIT이 사라지지는 않음

<br><br>

# Git Undoing

<br><br>

# TIL

Today I Learned<br>
그날 그날 배운 내용을 Markdown으로 문서화하여 정리

- [문서화 연습의 중요성](https://d2.naver.com/news/3435170)

### README.md

프로젝트에 대한 설명, 사용방법, 문서화된 정보 등을 알려주는 문서
