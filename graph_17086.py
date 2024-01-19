#아기상어2
# # 대각선포함 가장 짧은거리
# 1. visit 하지 않았고 1(상어0)칸을 찾기
# 2. dx,dy에 대하여 전부 0이면 길이 + 1,visited
# 3. 1에 도달하면 가장 최소, break
# 4. 그렇게 모든 위치 visit하면 거리들중 최소값
from collections import deque

def bfs(x,y):
  queue = deque()
  queue.append((x, y))
  visited[x][y]=True
  chk = [[0]*m for _ in range(n)]


  while queue:

    x,y=queue.popleft()



    for i in range (8):
        nx = x + dx[i]
        ny = y + dy[i]

        # shark=1일땐 visit 하고 break

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]  and shark[nx][ny]==1:

          queue.clear()
          chk[nx][ny]=chk[x][y]+1

          print(nx,ny)
          print(chk[nx][ny])
          return chk[nx][ny]
        elif nx==7 and ny==7:
          return 0
        chk[nx][ny]=chk[x][y]+1
        queue.append((nx, ny))




n,m=map(int,input().split())
visited = [[False for _ in range (m)] for _ in range(n)]

shark=[]
# n개줄의 상어값받기
for _ in range(n):
  shark.append(list(map(int, input().split())))

dx= [-1,1,0,0,1,1,-1,-1]
dy= [0,0,-1,1,1,-1,1,-1]
list=[]

#  shark 1  visited이 f일 때 체크
for i in range(n):
  for j in range(m):
    if shark[i][j]==1 and not visited[i][j]:
      list.append(bfs(i,j))


print(max(list))

