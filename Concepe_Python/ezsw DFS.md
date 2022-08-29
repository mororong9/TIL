### ezsw DFS

DFS 재귀호출

```python
def dfs(node):
    visited[node]=1
    print(node, end='')
	
    for next in range(n):
        if not visited[next] and graph[node][next]:
            dfs(next)

if __name__='__main__':
    n, e= map(int, input().split())
    visited=[0 for _ in range(n)]
    graph=[[0 for _in range(n)] for _ in range(n)] #인접행렬
    
    values=list(map(int, input().split())
    for i in range(e):
        u, v =values[i*2], values[i*2+1] #간선의 길이만큼 2개씩 값을 읽음
        graph[u][v]=graph[v][u]=1 #무방향
         
        dfs(0)
                
    
```



#### DFS - 스택활용

```python
def dfs(node):
    visited=[False for _ in range(n)] #로컬변수
    stack=[]
    stack.append(node)
    while stack:
        curr=stack.pop()
        if visited[curr]: continue
        
        visited[curr]=True
        print(curr, end='')
        for next in range(n):
            if not visited[next] and graph[curr][next]:
                stack.append(next)

if __name__=='__main__': #메인 모듈로 실행될때 실행됨
    n, e=map(int, input().split()) #전역변수임 함수가 아님
    graph=[[0 for _ in range(n)] for _ in range(n)]
    
    values= list(map(int, input().split()))
    for i in range(e):
        u,v=values[i*2], values[[i*2+1]
       	graph[u][vgraph[v][u]=1
        
   	dfs(0)
```



#### dfs -flood fill 알고리즘

상하좌우

입력

5

00000

00011

00010

11110#1은 벽

00000

113 #현위치 색칠하고자 하는값

```python
def dfs(r,c,color):
    visited=[[False for _ in range(n)] for _ in range(n)]
    stack=[]
    stack.append((r,c))
    while stack:
        curr=stack.pop()
        if visited[curr[0]][curr[1]]: continue
        
        visited[curr[0]][curr[1]]=True
        board[curr[0]][curr[1]]=color
        for i in range(4):
            nr=curr[0]+d[i][0]
            nc=curr[1]+d[i][1]
            if nr<0 or nr<n-1 or nc<0 or nc>n-1: continue
            if visited[nr][nc]: continue
            if board[nr][nc]==1: continue
            stack.append((nr))

if __name__=='__main__':
    D=((-1,0),(1,0),(0,-1),(0,1))
    n=int(input())
    board=[list(map(int, input().split())) for _ in range (n)] #상하좌우로 봐야하니까 배열
    
    sr,sc,color=map(int, input().split())
    dfs(sr,sc,color)
    
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()
```

