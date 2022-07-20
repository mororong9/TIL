```bash
to https://github.com/mororong/ITL
![rejected] master->master(fetch first)
#깃허브에 url보내려고 했음

error:failed to push some refs to 'https://github.com/mororong/ITL'
#에러남

#원격저장소에서 한 작업이 로컬에는 없다
#->원격저장소 커밋과 로컬 커밋이 다르다
hint: updates were rejected because the remote contatins work taht you do
hint:not have locally this is usually caused by another repository pushing
hint: to the same ref. 
#다시 push하기 전에 원격저장소 통합을 원할거다
you may want to first integrate the remote changes
hint: (e.g.'git pul'..) before pushing again
hint: see the 'note about fast-forwards' in ' git push --help' for details.
```

commits 눌러보면 버전이 다른걸 볼 수 있다 ( 깃에 해쉬값이 다름)

```bash
$git log --oneline
$git origin master
	merge branch~~~... ESC/wq로 나감
$git config --global core.editor "code --wait"-> vs창이 뜸 
$git push origin master
#커밋되면서 merge 커밋 내용이 뜸
$git log --oneline --graph 
#브랜치를 그래프로 보여줌
```

## github에 파일 숨기기

---

```bash
.gitignore
```

#깃 이그노어 파일안에 숨기고자 하는 넣는다 

[버전관리 필요없는것 모아놓은사이트](https://www.toptal.com/developers/gitignore/)

 -> ignore.io

#python #visualstudio #window

-> 해당 파일 .gitignore파일에 삽입

*이미 커밋된 파일은 반드시 삭제해야 .gitignore로 적용됨

### 상황1

```bash
git init
touch readme.md
git add .
git commit -m ' init'
git log

상황1 혼자 작업 (fast-forward)
-홈하면 만든다(home.txt)
1.브랜치 생성
1.feature/home branch 생성 및 이동
git branch feature/home(master) 
git checkout feature/home(master) 
2. 홈만듬
git home.txt(feature/home)
git add .(feature/home)
git commit -m '홈만듬'
3. 마스터 이동
git checkout master(feature/home)
4. 병합
git merge feature/home
git log --oneline
head-> master, feature/home 홈만듬
=>feature/home을 합침
5. 브랜치 삭제
git branch -d feature/home 
```

### 상황2

보고서파일+ 발표자료파일 각자 커밋이 발생했는데 다른 파일만 수정된 경우

```bash
1. about 브랜치 생성과 이동 동시에
git checkout -b about
2. 어바웃에서 작업
touch about.txt(about)
git add .
git commit -m '어바웃 만듬'
git log --oneline
3. master에서 작업
git checkout master
touch master.txt(master)
4. 머지함
git merge about(master)
git log --oneline --graph
merge branch about #어바웃 브랜치를 머지, 마스터에만 붙임
```

### 상황3

같은 파일이 수정되는 상황

```bash
1.test브랜치 생성, 이동
git checkout -b test
2. 리드미 수정 작업완료 후 커밋
git add .
git commit -m '리드미 수정함'

3. 마스터로 이동
git checkout master

4. 마스터에서도 리드미 수정 작업
git add .(master) #.은 수정한 부분을 말함
git commit -m '리드미 수정함'

5. 병합
git merge test(master)
->merge conflict
git status
->both modified
6. README.md 직접고침
git add .
git commit
git branch -d test
```

브랜치 병합과정에서 충돌-> 개발하는 방향에 맞게 고치기



## Folk로 push하기

```bash
git clone 폴크주소
git branch 브랜치이름
git checkout 브랜치이름 -> git checkout -b 브랜치이름
```





