#적록색약
#적,초 구분어렵
#영역 문제
#일반은 r,g,b로 세개 구분
#적록색약은 rg,b 로 두개 구분
# r,g,b 중 한 문자가 다음 문자랑 같으면  r이면 visit 1 g visit2 b visit 3
# 반복?
from collections import deque

def bfsR(x,y):
  queue=deque()
  queue.append((x,y))
  visited[x][y]=1
  while queue:

    x,y= queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<n and 0<=ny<n and graph[nx][ny]=='R' and visited[nx][ny]==0:
        queue.append((nx,ny))
        visited[nx][ny]=1


def bfsG(x,y):
  queue=deque()
  queue.append((x,y))
  visited[x][y]=1
  while queue:

    x,y= queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<n and 0<=ny<n and graph[nx][ny]=='G' and visited[nx][ny]==0:
        queue.append((nx,ny))
        visited[nx][ny]=1


def bfsB(x,y):
  queue=deque()
  queue.append((x,y))
  visited[x][y]=1
  while queue:

    x,y= queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<n and 0<=ny<n and graph[nx][ny]=='B' and visited[nx][ny]==0:
        queue.append((nx,ny))
        visited[nx][ny]=1


n= int (input())
graph=[]
for _ in range(n):
  graph.append(list(input()))


visited=[[ 0 ]*n for _ in range(n)]

dy=[0,0,1,-1]
dx=[1,-1,0,0]

count=0
for i in range(n):
  for j in range(n):
    if graph[i][j]=='R' and visited[i][j]==0:
      bfsR(i,j)
      count+=1
    elif graph[i][j]=='G' and visited[i][j]==0:
      bfsG(i,j)
      count+=1
    elif graph[i][j]=='B' and visited[i][j]==0:
      bfsB(i,j)
      count+=1


print(count)

count =0
visited=[[ 0 ]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if graph[i][j]=='G':
      graph[i][j]='R'

for i in range(n):
  for j in range(n):
    if graph[i][j]=='R':
      if visited[i][j]==0:
        bfsR(i,j)


        count+=1
    elif graph[i][j]=='B' and visited[i][j]==0:
      bfsB(i,j)
      count+=1


print(count)