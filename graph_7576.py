#토마토
#1은 익은 토마토, 0은 익지않은 토마토 -1은 토마토 없는 칸 상하좌우로만 영향 
#다 익기 위한 최소 일수
#1을 기준으로 0이면 +1
#-1은 생각X
#BFS로 graph를 +1해서 최대 graph에서 -1이 최소 일수
#0값이 하나라도 존재하면 -1 

from collections import deque
def bfs():
  queue=deque()
  for i in tomato:
    queue.append(i)

  while queue:
    x,y= queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]+1
        queue.append([nx,ny])








m,n= map(int,input().split())
tomato=[]

graph=[]
for _ in range(n):
  graph.append(list(map(int,input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
#1이 여러개일 경우를 생각해서
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      tomato.append([i,j])


bfs()
flag=False
Max=0

for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      flag=True
    elif graph[i][j]>Max:
      Max=graph[i][j]

if flag==True:
  print(-1)
else:
  print(Max-1)