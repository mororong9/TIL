#### Solution 팁

타입

숫자문제 -뒤집 개별값 알고싶다-시퀀스형태로 변환하면 좋지않을까 문자열로 바꿔서 뒤집을까

워드카운트 -기록해야하는데 알파벳 카운트 묶어야하네 키값-딕셔너리

수도문제 -숫자니까 int로 유지하는것이



갯수

내가 최댓값을 구하면서 위치까지 구해야해요

최소변수 2개 기록해야함 왜? 최대값 기록 따로 위치 따로



내가 무엇을 반복하고 위에서 정한 변수 중에 하나인것 , 어떤 결과를 만들지 생각

 어떤 조건에서 무엇을 바꿀지 



### List Comprehension

- 간단하게  리스트 만들기

```python
#방법1
list=[]
for num in range(1,4):
    list.append(num*3)
print(list)

#방법2
[num**3 for num in range(1, 4)]
#특정한 원소로 구성된 리스트를 만들때
```



### Dictionary Comprehension

```python
#방법 1
dict={}
for num in range(1, 4):
	dict[num]=num*3

```



### Lamda[parameter]:표현식 



```python
num=[1,3,5]

result=[]
for num in num:
	reuslt.append(num*3)
print(result)

#filter : 참인 요소만 꺼내는것
def multi(num):
    return num*3
print(list(map(multi,num))) #이 함수는 계속 사용되지않고 map에서만 사용

print(list(map(lamda n: n*3, num))) #lamda: 임시함수
#->
def mul3(n):
    return n*3==0
```



### PIP

- 파이썬 표준 라이브러리(PSL)-> 기존 설치되어있는것
- pip 설치

```bash
$pip install requests #패키지 설치
$pip list

$pip uninstall requests 
```



### 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip을 통해 설치
- vnenv: 가상환경을 실행하지 않으면 가장 기본(사용자 폴더)에 있는 파이썬으로 하는것(전역)
- 이 프로젝트 폴더에 파이썬  실행 패키지 



### Json

- 실시간 데이터 반영 가능

```python
import json
URL=
response=requests.get(URL).json()
print(response)
```

