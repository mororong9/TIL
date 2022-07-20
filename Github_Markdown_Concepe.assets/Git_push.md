## PUSH 충돌

```python
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
#commits 눌러보면 버전이 다른걸 볼 수 있다 ( 깃에 해쉬값이 다름)

$git log --oneline
$git origin master
	merge branch~~~... ESC/wq로 나감
$git config --global core.editor "code --wait"-> vs창이 뜸 
$git push origin master
#커밋되면서 merge 커밋 내용이 뜸
$git log --oneline --graph 
#브랜치를 그래프로 보여줌
```



