## 객체지향

```python
class rec:#클래스
    def __init__(self,x, y)
    self.x=x
    self.y=y
    
   def area(self):
   		return self.x*self.y #사각형 행동 기능:메서드
   def circumfer(self):
        return 2*(self.x+self.y)
r1=rec(10, 30)# r: 인스턴스 #사각형 정보 :속성
r1.area()
r1.circumfer()

```

```python
my_li=[1,2,3]
my_li.sort() #리스트에 데이터를 직접 정렬

my_li=[1,2,3]
sorted(my_li)#리스트는 sorted 함수의 인자로 전달될뿐 

#리스트: 클래스, 1,2,3: 인스턴스
```

클래스: canelCase로 쓴다

변수, 함수: snake_case로 쓴다

모든 클래스는 타입의 종류이다.

모든 인스턴스는 클래스로 표현가능

파이썬은 모든것이 객체 모든 객체는 특정 타입의 인스턴스이다



### 얕은 복사

```python
a= [1,2,3]
b=a #같은 주소에 할당 아예 b가 a의 주소를 갖게됨
b[0]='hi'

c=[3,4,5] #c=[3,4,5]
d=list(c) #다른 주소에 할당
d[0]='hi' #d=['hi',4,5]

e=[4,5,6] #e=[4,5,6]
f=e[::]
f[0]='hi' #f=['hi',5,6]


print(a)#['hi',2,3]같은 값 출력
print(b)#['hi',2,3]같은 값 출력-> 아예 주소가 바뀌기 때문

a='12345' #리스트 주소가 12345

```

### 깊은 복사

```python
a=[[1,2]2,3]
b=list(a)
b[0][0]='hi' #1차원상 리스트 주소가 달라졌음

import copy
d=[[1,2],2,3]
d=copy.deepcopy(c)  #내부 하위에 있는 주소를 카피를 따로 해서 저장
d[0][0]='hi'

print(a) #[[hi,2],2,3]
print(b) #[[hi,2],2,3]

```

### 객체 비교하기

```python
a=[1,2,3]
b=[1,2,3]
c=a
print(a==b, a is b)
#a,b,c 같다
```

### 인스턴스 메소드

- 인스턴스를 조작하기  위한 메서드
- 클래스 내부에 정의 되는 메서드의 기본
- 호출 시 첫 번 째 인자로 인스턴스 자기자신(self) 이 전달됨



### self

- 파이썬 인스턴스 메소드는 호출 시 첫번째 인자로 자기 자신이 전달됨

- 생성자 메소드: 인스턴스 객체가 생성될때 자동으로 호출되는 메소드

```python
class Person:
    def __init__(self,name):
        print('응애')
iu=Person('아이유') #응애
print(iu.name) #아이유

def greeting (self, ): #self 의 이름이 바뀔 수 있다
	self.name 
```

```python
t=int(input())
for test_case in range(1, t+1):
    a=map(int, input().split())
    print(list(a))
```