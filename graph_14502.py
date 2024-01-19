#14502
#연구소
#n*m크기의 연구소 상하좌우 바이러스
from collections import deque


n,m=map(int,input().split())
graph=[]

for _ in range(n):
  graph.append(list(input().split()))

print(graph)