#14502
#연구소
#실패
#n*m크기의 연구소 상하좌우 바이러스
#2를 찾고 주변을 1로바꿈 => 3개이하면 남은 0에 남은 벽수 뺴기
# 3개 이상이면 최소값찾아야함
# 한개를 감싸고 다른 한개를 남은벽을 감싸도 갯수가 남으면 1들을 이어서 0-0이 되어야 안전
# 너무많으면 3자리만 남아서 3개 리턴


#2주변에 1을 0-0이 되게 만든다.
# 이때 벽이 3개 이상이면 다시 
#실패

# 바이러스 퍼트리는 함수
# 0인부분중 벽 3개의 모든 경우를 골라 체크
# 이중에서 가장 큰수 

from collections import deque
from itertools import combinations
import copy

def bfs(Chkgraph):
  # 바이러스 퍼트리고 안전 영역 체크함수
  queue=deque()
  for i in virus:
    queue.append(i)
  
  while queue:
    x,y= queue.popleft()
    
    for i in range (4):
      nx=x+ dx[i]
      ny=y+ dy[i]
      
      if 0<=nx<n and 0<=ny<m:
        if Chkgraph[nx][ny]==0:
            Chkgraph[nx][ny]=2
            queue.append((nx,ny))
  
  safeN=0
  for i in range(n):
    for j in range(m):
      if Chkgraph[i][j]==0:
        safeN+=1
        
  return safeN
  

n,m = map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

graph=[]
for _ in range(n):
  graph.append(list(map(int, input().split())))

area=[]
virus=[]
for i in range(n):
  for j in range (m):
    if graph[i][j]==0:
      area.append([i,j])
    elif graph[i][j]==2:
      virus.append([i,j])
result=0  
chk=0   
Combi_Wall=combinations(area,3)

for Combi in Combi_Wall:
    Chkgraph=copy.deepcopy(graph) 

    # 3개 조합 만들기
    for idx in range(3):
        Chkgraph[Combi[idx][0]][Combi[idx][1]]=1
    chk=bfs(Chkgraph)
    if chk> result:
      result=chk
print(result)
    
#from collections import deque

#def find(x,y):
#  queue = deque()
#  queue.append((x,y))

#  while queue:
#    x,y = queue.popleft()
#    for i in range(4):
#      nx = x + dx[i]
#      ny = y + dy[i]
#      if 0<= nx <n and 0<=ny<m :
#        continue
#      if graph[nx][ny] == 0:
#        graph[nx][ny] = 2
#        queue.append((nx,ny))
     

#def area():
#  queue = deque()
#  queue.append((0,0))
#  count=0
#  while queue:
#    x,y=queue.popleft() 
#    for i in range(4):
#      nx=x+dx[i]
#      ny=y+dy[i]
#      if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny]==0:
#        visited[nx][ny]=1
#        queue.append((nx,ny))
#        count+=1
        
#  return count



#n,m=map(int,input().split())

#visited=[[0]*m for _ in range(n)]
#graph=[]
#for _ in range(n):
#  graph.append(list(input().split()))

#dx=[-1,1,0,0]
#dy=[0,0,-1,1]
#list=[]
#for i in range(n):
#  for j in range(m):
#    if graph[i][j]== 2:
#      list.append([i,j])
      

