#16234
#인구이동
# 인구차이가 l이상r이하이면 경계선오픈
# 인접나라총인구//나라수로 인구 조정
#특정없이 나라의 좌우상하를 l r로 비교
# 가능하면 ++
# visited하고 더해진 나라도 탐색
# 다방문할떄까지 탐색
# 이전체가 하루 

from collections import deque

def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  visited[x][y]=1
  country=[]
  country.append((x,y))
  total=data[x][y]
  num=1
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n :
        if l<=abs(data[x][y]-data[nx][ny])<=r and visited[nx][ny]==0:
          visited[nx][ny]=1
          num+=1
          country.append((nx,ny))
          total+=data[nx][ny]
          queue.append((nx,ny))
  change=total//num
  for i in country:
    data[i[0]][i[1]]=change
    
  
      
    


n,l,r=map(int,input().split())
data=[[0]*n for _ in range(n)]
for i in range(n):
  data[i]=list(map(int,input().split()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

Day=0
while True :
  chk=0
  visited=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if visited[i][j]==0:
        bfs(i,j)
        chk+=1
    
    
  if chk==0:
    break
  Day+=1

print(Day)

      