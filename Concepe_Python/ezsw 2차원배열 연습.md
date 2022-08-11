### ezsw 2차원배열 연습

2차원배열 십자가 출력

```python
row, col=map(int,input().split())
board=[list(map(int, input().split())) for _ in range(row)]
sr,sc=map(int, input().split())

def cross():
    if board[sr][sc] != 0:
        return
    board[sr][sc]=1
    
    for i in range(sr-1,-1,-1): # 위로 올라갈거니까 감소!!(항상배열로 생각)
        if board[i][sc] !=0: #0이 아니면 중단
            break
        board[i][sc]=1 #0이면 1로 채움
    #이제 아래로 내려갈거임
    for i in range(sr+1, row):
        if board[i][sc] !=0:
            break
        board[i][sc]=1
        
    #왼쪽
   	for j in range(sc-1,-1,-1):
        if board[sr][j]!=:
            break
        board[sr][j]=1
    
    #오른쪽
    for j in rnage(sr+1,col):
        if board[sr][j] !=0:
            break
        board[sr][j]=1
     
    cross()
    
    #출력
    for i in range(row):
        for j in range(col):
            print(board[i][j], end=' ')
    print()
```

입력

5 5

00000

00020

00000

22200

00000

11

#### 재귀호출

```python
def factoriial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

factorial(3)-> 
def factorial(3):
    ..
    return 3*factorial(2)->
...
def factorial(0):
    if 0==0:
        return 1  #pop된다
    
    
import sys
sys.setrecursionlimit(1500) # 최대 호출 제한
```



#### flood fill 알고리즘

입력 5

00000

00011  #1,1 부터 0을 1로채운다

00010

11110

00000

11 #시작 위치

```python
def fill(r,c): #r 행, c 열 을 받는다
    if r<0 or r>n-1 or c<0 or c>n-1:
        return
    if board[r][c] !=0:
        return
    board[r][c]=1
    fill(r-1, c)
    fill(r+1, c)
    fill(r, c+1)
    fill(r, c-1)
    

n=int(input())
board=[list(map(int, input().split()))for _ in range(n)] #행갯수만큼 열 입력받음
strow, stcol=map(int, input().split())

fill(strow,stcol) #함수에 행열을 전달

```

