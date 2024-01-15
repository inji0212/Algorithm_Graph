#나이트 이동
#이동 최소 거리
from collections import deque

def move(x,y):
  queue = deque()
  queue.append((x, y))
  visited=[[0 for _ in range(L) ] for _ in range(L)]
  visited[x][y]=1

  while queue:
    x, y = queue.popleft()
    if visited[x][y]==1 and graph[x][y]==1:
      return 0
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]


      if 0<= nx<L and 0<=ny<L:

        if visited[nx][ny]==0 and graph[nx][ny]==1:

          visited[nx][ny]=visited[x][y]+1     

          return visited[nx][ny]-1
        elif visited[nx][ny]==0 and graph[nx][ny]==0:

          visited[nx][ny]=visited[x][y]+1  
          queue.append((nx, ny))




T= int(input())
dx=[1,1,2,2,-1,-1,-2,-2]
dy=[2,-2,1,-1,2,-2,1,-1]

for _ in range(T):
  L= int(input())
  graph = [[0 for _ in range (L)] for _ in range(L)]

  x1,y1=map(int, input().split())



  x2,y2=map(int, input().split())
  graph[x2][y2]=1
  print(move(x1,y1))


