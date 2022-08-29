### 이차원리스트 DFS단골문제

#### 그림

```python
def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])
     
graph=[]    
    
for _ in range(n):
    graph_list=lisit(map(int, input().split()))
    graph.append(graph_list)

visited=[]
for _in range(n):
    visited_list=[False]*m
    visited.append(visited_list)

dy=[-1,0,0,0]
dx=[0,1,0,-1]
    
for sy in range(n):
    for sx in range(m):
        if not visited[sy][sx] and graph[sy][sx]==1:
        stack=[]
        stack.append([y,x])
        visited[y][x]=True
       
    	while len(stack)!=0:
            node=stack.pop()
            
            for d in range(4):
                ny=y+dy[d]
                nx=x+dx[d]
                
                if(-1<ny< n and -1<nx<m):
                    continue
                if visited[ny][nx]==True:
                    continue
                if graph[ny][nx]!=1:
                    continue 
                stack.append((ny, nx))
if len(painting_size_list)           
	print(painting_count)
	print(max(painting_size_list))
else:
	print()
```

