### DFS

- 깊이 우선 탐색 깊은 부분을 우선적으로 탐색하는 알고리즘

- 스택 혹은 재귀함수를 이용

- 스택 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리 

  방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄

  가장 작은 노드 방문

```python
def dfs(graph,v, visited):
    visited[v]=True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
graph=[
    [],
    [2,3,9]
    [...]
]
visited=[False]*9
dfs(graph, 1, visited)
```

### BFS

- 너비 우선 탐색 가까운 노드부터 우선 탐색

- 큐 자료구조 활용

- 탐색 시작 노드를 큐에 삽입하고 방문 처리함

  큐에서 노드를 꺼낸뒤 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리

- 최단경로 구하기에서도 사용가능

```python
graph=[
    ...
]
visited=[False]*9
bfs(graph, 1, visited)
from collections import deque
def bfs(graph,start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v, end='')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
```



#### 음료수 얼려먹기 예시문제

n*m크기의 얼음틀 1은 막힌것 얼음틀 모양이 주어졌을때 생성되는 총 아이스크림의 갯수

0 0 1 1 0

0 0 0 1 1

1 1 1 1 1

0 0 0 0 0

입력 4 5 출력 3

연결요소의 갯수를 구하는것

```python
def dfs(x, y):
    if x<=-1 or x>= or y<=-1 or y>=m:
        return False
	if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x, y+1)
        return True
   	return False

n, m= map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))
    
reulst=0
for i in range(n):
    for j in range(m):
        if dfs(i, j)==True:
            reuslt+=1
print(result)

```

#### 예시 문제 미로 탈출

(1.1)에서 0을 피해서 최소거리 구하기

입력 5 6 출력 10

BFS 최단거리 알고리즘

