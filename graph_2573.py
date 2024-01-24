#2573
#빙산 
# 주위에 0의 갯수만큼 줄어든다. 최소는 0
# 두덩얼 ㅣ이상 분리되는 최초 시간
# 다녹을때까지 분리안되면 0
# 하나당 주위 0을 빼고 영역체크?
# 해당된 수를 빼고 영역체크
from collections import deque

def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  visited[x][y]=1

  while queue:
    cnt=0
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<= nx<n and  0<=ny<m :
        # 0이면 뺴기 위해 카운트
        # 숫자가 있으면 다음 체크를 위해 append
        if graph[nx][ny]==0 and visited[nx][ny]==0:
          cnt+=1
        elif graph[nx][ny]>0 and visited[nx][ny]==0:
          visited[nx][ny]=1
          queue.append((nx,ny))
    if graph[x][y]-cnt>0:
      graph[x][y]-=cnt
    else:
      graph[x][y]=0
      visited[x][y]=1
  #각 자리에서 0갯수만큼 뺴고 다음 숫자는 queue에 반복


n,m= map(int,input().split())
graph=[]
visited=[[0]*m for _ in range(n)]
for _ in range(n):
  graph.append(list(map(int,input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
year=0
while 1:

  count=0
  visited=[[0]*m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if graph[i][j]>0 and visited[i][j]==0 :
        bfs(i,j)
        count+=1
  # 카운트가 1개이면 아직 한덩어리라서 계속진행
  # 카운트가 2개이상이면 덩어리가 여러개인거라서 end
  # 카운트가 0개이면 다녹을떄까지 분리가 안된거
  if count>=2:
    print(year)
    break
  elif count==0:
    print(0)
    break
  year+=1 
#만약 빙하가 분리가 안되면 