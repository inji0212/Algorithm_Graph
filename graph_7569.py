from collections import deque

def bfs():
  queue=deque()
  for i in tomato:
    queue.append(i)

  while queue:
    z,x,y=queue.popleft()
    for i in range(6):
      nx=x+dx[i]
      ny=y+dy[i]
      nz=z+dz[i]
      if 0<=nx<n and 0<=ny<m and 0<= nz<h and graph[nz][nx][ny]==0:
        graph[nz][nx][ny]=graph[z][x][y]+1
        queue.append([nz,nx,ny])

m,n,h= map(int, input().split())
dx= [-1,1,0,0,0,0]
dy= [0,0,-1,1,0,0]
dz= [0,0,0,0,-1,1]

graph=[[] for _ in range(h)]
for i in range(h):
  for _ in range(n):
    graph[i].append(list(map(int,input().split())))

tomato=[]

for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k]==1:
        tomato.append((i,j,k))

bfs()

flag=False
Max=0
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k]==0:
        flag=True
      elif graph[i][j][k]>Max:
        Max=graph[i][j][k]

if flag==True:
  print(-1)
else:
  print(Max-1)