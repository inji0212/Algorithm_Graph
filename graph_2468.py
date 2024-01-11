# 1~n까지 의 높이체크
# k만큼 각자리 수들을 뺀다. 
# 이때 각 자리에서 주변이 0이면 영역+1
# 접하는 영역은 처음만+1하고 다른 영역 나올떄까지 0

from collections import deque

def bfs():
  queue= deque()
  queue.append(0)
for chk in range(n):
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 1:
          graph[i][j]-=n
          queue.append((i,j))
          graph[i][j] = 0
        
n= int(input())

graph=[]
for _ in range(n):
  graph.append(list(map(int,input().split())))
print(graph)
dx=[-1,1, 0,0]
dy=[0,0, -1,1]
chk=0
visited=[[0 for _ in range(n)] for _ in range(n)]