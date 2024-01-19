#스타트링크
#총f층 G층에 위치 현재 s층
#u버튼 위로 u층 d버튼 아래로 d층
#갈수 없다면 "usethe stairs"
#확인 유닛을 u,d로
#리스트처럼 생각해서 s시작해서 g까지 버튼수 

from collections import deque

def bfs(s):
  queue=deque()
  queue.append(s)
  visited[s]=1
  while queue:
    x=queue.popleft()
    if x==g:
      return visited[x]-1
    for i in range(2):
      nx=x+dx[i]
      if 0<nx<=f and visited[nx]==0:
        visited[nx]=visited[x]+1
        queue.append(nx)


  return -1      


f,s,g,u,d = map(int, input().split())

dx=[u,-d]
visited=[0]*(f+1)


chk=bfs(s)
if chk==-1:
  print("use the stairs")

else:
  print(chk)