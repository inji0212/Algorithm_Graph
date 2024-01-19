#9205
#맥주마시면서 걸ㅇㅓ가기

#맥주 20개 50미터당 한병
#ㅠㅕㄴ의점 빈병버리고 맥주살수있다. 박스에 20병이하 ㅠㅕㄴ의점에서 맥주 한병 마시기
#상근ㅇ ㅣ집 편의점 페스티벌
# 성공은 해피 실패 새드
#좌표사이 거리는 x+y
# 좌표와 페스티벌 사이 거리 합이 1000이하면 성공
# 현 좌표는 홈에서 편의점까지 성공했을때.

from collections import deque

def bfs(x,y):
  
  queue=deque()
  queue.append((x,y))

  
  while queue:
    x,y=queue.popleft()
    
    if abs(fest1-x)+abs(fest2-y)<=1000:
      #현 좌표와 페스티벌 사이거리가 1000일때
      return 'happy'
      
    #편의점 도달하면 맥주 20개되니까
    #현좌표에서 1000이하고 가장 가까운 편의점
    for i in range(n):
      if abs(mid[i][0]-x)+abs(mid[i][1]-y)<=1000 and visited[i]==0:
        visited[i]=1
        queue.append((mid[i][0],mid[i][1]))
        
  return 'sad'
     
 
  


t= int(input())

for _ in range(t):

  n= int(input())
  x1,y1=map(int, input().split())
  visited=[0]*n
  mid=[]
  for _ in range(n):
    x,y= map(int,input().split())
    mid.append((x,y))
 
  fest1,fest2=map(int, input().split())
  print(bfs(x1,y1))
 

  # 50미터당 한병이니 
  # 1 그냥 페스티벌갈때 
  # 2 편의점 들려서 편의점 갈떄 
  # 좌표에서 좌표갈떄 차이/50 갯수필요 가능할때
  # 20-갯수 더해져서 나오기 
  # 다시 좌표에서 페스티벌가기

