#1987
#알파벳
#R*C 0,0 말
# 말 상하좌우 네칸 이동하고 다른 알파벳칸만 이동가능
# 문자 코드로 찾기 

def dfs(x,y,visited):
  global cnt
  

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in visited:
      dfs(nx,ny,visited+graph[nx][ny])

  cnt= max(cnt, len(visited))


r,c=map(int,input().split())

graph=[]

for _ in range(r):
  graph.append(list(input()))


dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
dfs(0,0,graph[0][0])
print(cnt)
